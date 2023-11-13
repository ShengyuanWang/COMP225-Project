from flask import Flask, request, render_template
from markupsafe import escape
import json
import random
import requests
from flask_cors import CORS
import re
from textblob import TextBlob

# DO NOT make this public, keep in private github
API_KEY = "AIzaSyAHHByDAWIAvXhTNkajTqazMhBUO045aS0" 

 # update this when new genres added to alcohol json

with open("output.json") as file:
    jsonData = json.load(file)
GENRES = jsonData

# drink for when there are no matches 
BUD_LIGHT = {"name":"Bud Light", "instructions": ["Just pop open the can."], "information": "Classic American Beer."}

app = Flask(__name__)
CORS(app)

@app.route('/', methods =["GET", "POST"])
def get_book():
    """ Return rendering of home.html template. Handles user input and 
    displays results for testing. 
    """

    if request.method == "POST":
        user_input = escape(request.form.get("book"))
        book = Book(user_input)
        return render_template("home.html", user_input=book.get_user_input(), title=book.get_title(),
                                isbn_list=book.get_isbn_list(), isbn=book.get_isbn(),
                                authors=book.get_authors(), publisher=book.get_publisher(),
                                date=book.get_publication_date(), genres=book.get_genres(),
                                filtered_genres=book.get_filtered_genres(), description=book.get_description(),
                                cover_link=book.get_cover_link(), drinks=[drink["name"] for drink in book.get_matching_drinks()],
                                pairing=book.get_pairing())
    return render_template("home.html")

@app.route('/test/<bookname>', methods=["GET"])
def search1(bookname):
    """Return pairing dictonary for testing of frontend intergration."""
    book = Book(bookname)
    return book.get_pairing_json_obj()


class Book:
    def __init__ (self, user_input, alcohol_data_file="book-alcohol-pairings.json", api_key=API_KEY, official_genres=GENRES, no_match_drink=BUD_LIGHT):
        """ This class represents a book. Once an object of this class is initiated, that object can be
        used to query book data and get pairings for the book.
        
        Keyword arguments:
        user_input -- string of title inputted by user
        alcohol_data_file -- json dump containing data for alcohol (default "book-alcohol-pairings.json")
        api_key -- string of api key for google api (default API_KEY constant) 
        offical_genres -- list of genres used in alcohol data file (default OFFICAL_GENRES constant) 
        no_match_drink -- string of drink to use if no pairing found (default "Bud Light")
        """
        self.user_input = user_input
        self.alcohol_data_file = alcohol_data_file
        self.api_key = api_key
        self.official_genres = official_genres
        self.no_match_drink = no_match_drink

        self.isbn_list = self.query_api_isbns(self.user_input)
        self.isbn = self.select_isbn(self.isbn_list)
        self.data = self.query_api_book_data()
        self.genres = self.query_api_genres()

    def get_pairing_json_obj(self):
        """ Returns a json object containing book data and pairing for
        use in frontend.
        """
        pairing = {}
        pairing["title"] = self.get_title()
        pairing["authors"] = self.get_authors()
        pairing["genres"] = self.get_filtered_genres()
        pairing["cover_link"] = self.get_cover_link()
        pairing_dict = self.get_pairing()
        pairing["name"] = pairing_dict["name"]
        pairing["instructions"] = pairing_dict["instructions"]
        pairing["information"] = pairing_dict["information"]
        return json.dumps(pairing)

    def get_pairing(self):
        """ Return pairing for book. Takes matching drink and 
        randomly returns one drink as the pairing. If no drink is found,
        returns the drink specfied as the no-match drink.
        """
        drinks = self.get_matching_drinks()
        drink_dict = {}
        if len(drinks) > 0:
            ran_drink = random.choice(drinks)
            drink_dict["name"] = ran_drink["name"]
            drink_dict["instructions"] = ran_drink["instructions"]
            drink_dict["information"] = ran_drink["information"]
            return drink_dict
        else:
            return self.get_no_match_drink()

    def get_matching_drinks(self):
        """ Return list of drinks that match book based on data in json file. 
        If no drinks match, returns an empty list. Drinks are represented as
        dictonaries. 
        """
        genres = self.get_filtered_genres()
        with open(self.alcohol_data_file, "r") as f:
            drinks = json.load(f)
        matched_drinks = []

        if genres is not None and len(genres) > 0:
            for drink in drinks["alcohols"]:
                for genre in genres:
                    if genre in drink["genres"]:
                        if all(key in drink for key in ["name", "type", "genres", "sentiment", "instructions", "information"]):
                            matched_drinks.append(drink)
        return matched_drinks

    def get_sentiment(self):
        blob = TextBlob(self.get_description())
        sentiment_score = blob.sentiment.polarity
        return round(sentiment_score, 2)

    def query_api_isbns(self, title):
        base_url = 'https://www.googleapis.com/books/v1/volumes'
        params = {
            'q': f'intitle:{title}',
            'key': self.api_key
        }
        isbns = []
        try:            
            data = requests.get(base_url, params=params).json()['items']
            title = ""
            counter = 0
            for entry in data:
                volume_info = entry.get('volumeInfo', {})
                isbn = volume_info.get('industryIdentifiers', [])[0]
                if isbn.get("type") == "ISBN_13":
                    if counter == 0:
                        title = self.filter_title(volume_info["title"])
                        isbns.append(isbn.get("identifier"))
                    if self.filter_title(volume_info["title"]) == title:
                        isbns.append(isbn.get("identifier"))
                    counter += 1
            return isbns
        except:
            return isbns
    

    def query_api_book_data(self):
        """Return a dict of book data, or an empty dictonary 
        if api query fails. Queries google books api using isbn. 
        """
        base_url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": f"isbn:{self.isbn}",
            "key": self.api_key
        }
        
        if len(self.isbn) > 0:
            try:
                data = requests.get(base_url, params=params).json()
                return data["items"][0]["volumeInfo"]
            except:
                return {}
        else:
            return {}

    def query_api_genres(self):
        """Return a list of all genres the book has, or an empty list 
        if api query fails. Queries openlibrary api using isbn. 
        """
        genres = []
        try:
            for isbn in self.isbn_list:
                base_url = "https://openlibrary.org/api/books"
                params = {
                    "bibkeys": f"ISBN:{isbn}",
                    "format": "json",
                    "jscmd": "data"
                }
                json = requests.get(base_url, params=params).json()
                data = json.get(f"ISBN:{isbn}", {})
                names = self.split_subjects(data.get('subjects', ['N/A']))   
                print(names)
                names = self.combine_dates(names)             
                genres += names
            return genres
        except:
            return genres
    
    def split_subjects(self, subjects):
        """ This function takes a list of dictonaries of book subjects and splits the subject names 
        into smaller parts. The dictonaries must have at least the key "name". Subject names 
        will be split based on commas, dashes, em dashes. Phrases inside parenthese will also
        be extracted. Subject names will be made lowercase and trailing spaces are removed.
        """
        names = []
        for subject in subjects:
            if isinstance(subject, dict):
                regex_split = re.split(r"[,—–/]", subject["name"])
                for word in regex_split:
                    word = word.strip().lower()
                    if "(" in word:
                        part_split = word.split("(")
                        names.append(part_split[0])
                        if len(part_split) > 1 and len(part_split[1]) > 1:
                            if part_split[1][len(part_split[1])-1] == ")":
                                names.append(part_split[1][:len(part_split[1])-1])
                            else:
                                names.append(part_split[1])
                    else:
                        names.append(word.strip())
        return [name for name in names if name != ""]
    
    def combine_dates(self, list_of_genres):
        newGenres = []
        print(list_of_genres)
        for name in list_of_genres:
            #print(name)
            #if '9' in name or '2' in name or '3' in name or '4' in name or '5' in name and ('-' in name):
                #name = name.split('-')
            if '1939-1945' in name:
                #World war II/20th century for 1939-1945
                newGenres.append('world war ii')
                newGenres.append('20th century')
            else:
                newGenres.append(name) 

        #print(newGenres)
        return newGenres

    def filter_title(self, title):
        """Cleans up titles to not include some common stop words, so that the titles 
        can be more easily matched. Used when looking for genres across all 
        versions of a book.
        """
        # idea: find titles based on author and key words from titles
        words = title.split()    
        filtered_words = [word for word in words if word.lower() not in ["and", "a", "the"]]
        filtered_phrase = ' '.join(filtered_words)
        return filtered_phrase
    
    def select_isbn(self, isbns):
        """Selects the first isbn from the list of isbns."""
        if len(isbns) > 0:
            return isbns[0]
        else:
            return ""

    def get_filtered_genres(self):
        """Return a list of all the offical genres the book has or an empty list 
        if the book has no offical genres.
        """
        filtered_genres = []
        for genre in self.genres:
            if genre in self.official_genres:
                    filtered_genres.append(genre)
        return filtered_genres

    def get_title(self):
        """Using book data dictonary, return title found for the book, 
        or an empty string if no title was found.
        """
        if "title" in list(self.data.keys()):
            return self.data["title"]
        else:
            return ""

    def get_authors(self):
        """Using book data dictonary, return list of authors found for the book, 
        or an empty list if no authors were found."""
        if "authors" in list(self.data.keys()):
            return self.data["authors"]
        else:
            return []

    def get_description(self):
        """Using book data dictonary, return description found for the book, 
        or an empty string if no description was found."""
        if "description" in list(self.data.keys()):
            return self.data["description"]
        else:
            return ""

    def get_publisher(self):
        """Using book data dictonary, return publisher found for the book, or 
        an empty string if no publisher was found.
        """
        if "publisher" in list(self.data.keys()):
            return self.data["publisher"]
        else:
            return ""

    def get_publication_date(self):
        """Using book data dictonary, return publication date found for the book, 
        or an empty string if no publication date was found.
        """
        if "publishedDate" in list(self.data.keys()):
            return self.data["publishedDate"]
        else:
            return ""

    def get_cover_link(self):
        """Using book data dictonary, return the link to the 
        small thumbnail image of the book's cover, or an empty string if no 
        thumnbail was found.
        """
        if "imageLinks" in list(self.data.keys()):
            if "smallThumbnail" in list(self.data["imageLinks"].keys()):
                return self.data["imageLinks"]["smallThumbnail"]
        return ""

    def get_isbn(self):
        """Return the instance variable containing the book's ibsn, will be the 
        first one found in the google books api query."""
        return self.isbn

    def get_isbn_list(self):
        """Return the instance variable containing the list of the books's ibsns."""
        return self.isbn_list

    def get_user_input(self):
        """Return the instance variable containing the title the user inputed."""
        return self.user_input

    def get_genres(self):
        """Return the instance variable containing a list of all genres found 
        for book.
        """
        return self.genres

    def get_no_match_drink(self):
        """Return the instance variable containing the drink object that will be used if 
        no pairing is found. Must have the keys name, instructions, information.
        """
        return self.no_match_drink

if __name__ == "__main__":
    app.run(port=8000)