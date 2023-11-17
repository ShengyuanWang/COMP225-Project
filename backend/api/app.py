from flask import Flask, request, render_template
from markupsafe import escape
from flask_cors import CORS
from textblob import TextBlob
import json
import requests
import re
import heapq

# DO NOT make this public, keep in private github
API_KEY = "AIzaSyAHHByDAWIAvXhTNkajTqazMhBUO045aS0" 

 # update this when new genres added to alcohol json

with open("output.json") as file:
    jsonData = json.load(file)
GENRES = jsonData

# drink for when there are no matches 
BUD_LIGHT = {"name":"Bud Light", "ingredients": ["Can of bud light"], "instructions": "Just pop open the can."}

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
                                cover_link=book.get_cover_link(), pairing_json_obj=book.get_pairing_json_obj(), 
                                top_matches=[drink["name"] for drink in book.get_top_drink_matches(book.get_matching_drinks())],
                                all_matches=book.drink_heap_to_ordered_list(book.get_matching_drinks()), 
                                pairing=book.get_pairing(),  sentiment=book.get_sentiment())
    return render_template("home.html")

@app.route('/test/<bookname>', methods=["GET"])
def search1(bookname):
    """Return pairing dictonary for testing of frontend intergration."""
    # bookname = bookname.replace("%20", " ")
    book = Book(bookname)
    return book.get_pairing_json_obj()

class DrinkWrapper():
    def __init__(self, drink_data, priority):
        """ This is wrapper class for drink data for creating the priority queue.
        It contains a cutsom comparator which python's heapq needs to create a 
        priority queue.
        """
        self.priority = priority
        self.drink_data = drink_data

    def get_drink_data(self):
        return self.drink_data 

    def get_priority(self):
        return self.priority 
    
    def __str__(self):
        return f"Priority: {self.priority}, Data: {self.drink_data}"

    def __lt__(self, other):
        return self.priority < other.priority

@app.route('/getAlcohol/<types>', methods=["GET"])
def get_alcohol(types):
    with open('book-alcohol-pairings.json', "r") as f:
        drinks = json.load(f)

    drinks_filtered = []
    for drink in drinks['alcohols']:
        if drink["type"] == types:
            drinks_filtered.append(drink)
    return json.dumps(drinks_filtered)



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
        pairing["user_input"] = self.get_user_input()
        pairing["title"] = self.get_title()
        pairing["authors"] = self.get_authors()
        pairing["genres"] = self.get_filtered_genres()
        pairing["cover_link"] = self.get_cover_link()
        pairing_dict = self.get_pairing()
        pairing["name"] = pairing_dict["name"]
        pairing["ingredients"] = pairing_dict["ingredients"]
        pairing["instructions"] = pairing_dict["instructions"]
        return json.dumps(pairing)

    def get_pairing(self):
        """ Return pairing for book. Takes matching drink and 
         returns drink with sentiment score most similar to book. 
        If no matching drinks, returns the drink specfied as the no-match drink.
        """
        all_drinks = self.get_matching_drinks()
        top_drink_matches = self.get_top_drink_matches(all_drinks)
        sentiment = self.get_sentiment()
        
        if len(top_drink_matches) > 0:
            pairing = min(top_drink_matches, key=lambda drink_match: abs(drink_match["sentiment"] - sentiment))
            return pairing
        else:
            return self.get_no_match_drink()
       
    def get_matching_drinks(self):
        """ Return priority queue of drinks that match book based on data in json file. 
        If no drinks match, returns an empty list. Prority is based both on how many genres
        a book and drink share and how many they don't share.
        It's calculated like this:
            number of shared genres - (.1 * number of genres not shared )
        Drinks are added to the priority queue by wrapping 
        them in the DrinkWrapper class, which contains a custom comparator. The priority queue
        is implmented with python's heapq module and is a max-heap.
        """
        book_genres = self.get_filtered_genres()
        with open(self.alcohol_data_file, "r") as f:
            drinks = json.load(f)
        matched_drinks = []
        heapq.heapify(matched_drinks)

        if book_genres is not None and len(book_genres) > 0:
            for drink in drinks["alcohols"]:
                shared_genre_count = 0
                unshared_genre_count = 0
                for drink_genre in drink["genres"]:
                    if drink_genre in book_genres:
                        shared_genre_count += 1
                    else:
                        unshared_genre_count += .1
                if shared_genre_count > 0:
                    genre_count = round(shared_genre_count - (unshared_genre_count), 2)
                    heapq.heappush(matched_drinks, DrinkWrapper(drink, genre_count))
        heapq.heapify(matched_drinks)
        return matched_drinks
    
    def get_top_drink_matches(self, drink_heap, range=.2):
        """ Takes the max heap of the drink and returns the drink data dicts that share the 
        highest priority.
        """
        top_priority = heapq.nlargest(1, drink_heap)[0].get_priority() if drink_heap else None
        top_matches = []
        for drink_obj in drink_heap:
            if drink_obj.priority >= top_priority - range:
                top_matches.append(drink_obj.get_drink_data())

        if len(top_matches) < 3:
            heap_list = self.drink_heap_to_ordered_list(drink_heap)
            if len(heap_list) >=  3:
                top_matches = [drink_obj.get_drink_data() for drink_obj in heap_list[:3]]
            else:
                top_matches = [drink_obj.get_drink_data() for drink_obj in heap_list[:len(heap_list)]]
       
        return top_matches

    def drink_heap_to_ordered_list(self, drink_heap):
        """ Turns a heap into an ordered list, where the first element in the list 
        is the entry in the heap with the highest priority."""
        secure_copy = drink_heap[:]
        ordered_list = []
        while secure_copy:
            element = heapq.heappop(secure_copy)
            ordered_list.append(element)
        return ordered_list[::-1]

    def get_sentiment(self):
        """ Uses TextBlob to get the sentiment score of the book.
        Gets the sentinent score of the unfiltered genres and the description,
        then averages them together and rounds to two decimal places.
        """
        genres_string = ",".join(self.get_genres())
        genre_blob = TextBlob(genres_string)
        genre_sent = genre_blob.sentiment.polarity

        desc = self.get_description()
        desc_blob = TextBlob(desc)
        desc_sent = desc_blob.sentiment.polarity

        sentiment = (genre_sent + desc_sent) / 2
        return round((sentiment), 2) 
    
    def query_api_isbns(self, title):
        """ Gets all isbns for a given book using google book API and user input.
        Assumes the correct title is the first result, and from there, ignoring  
        major stop words and common punctutaion, returns a list of all isbns
        that share the same title as the first result.
        """
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
        """ Return a dict of book data, or an empty dictonary 
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
        """ Return a list of all genres the book has, or an empty list 
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
                
                names_split = self.split_subjects(data.get('subjects', ['N/A'])) 
                names_dates_combined = self.combine_dates(names_split)             
                genres += names_dates_combined
            return genres
        except:
            return genres
        
    def filter_title(self, title):
        """ Cleans up titles to not include some common stop words, so that the titles 
        can be more easily matched. Used when looking for genres across all 
        versions of a book.
        """
        # idea: find titles based on author and key words from titles
        words = title.split()    
        filtered_words = [word for word in words if word.lower() not in ["and", "a", "the"]]
        filtered_phrase = ' '.join(filtered_words)
        return filtered_phrase
    
    def split_subjects(self, subjects_to_split):
        """ This function takes a list of dictonaries of book subjects and splits the subject names 
        into smaller parts. The dictonaries must have at least the key "name". Subject names 
        will be split based on commas, dashes, em dashes. Phrases inside parenthese will also
        be extracted. Subject names will be made lowercase and trailing spaces are removed.
        """
        new_names_split = []
        for subject in subjects_to_split:
            if isinstance(subject, dict):
                regex_split = re.split(r"[,—–/]", subject["name"])
                for word in regex_split:
                    word = word.strip().lower()
                    if "(" in word:
                        part_split = word.split("(")
                        new_names_split.append(part_split[0])
                        if len(part_split) > 1 and len(part_split[1]) > 1:
                            if part_split[1][len(part_split[1])-1] == ")":
                                new_names_split.append(part_split[1][:len(part_split[1])-1])
                            else:
                                new_names_split.append(part_split[1])
                    else:
                        new_names_split.append(word.strip())
        return [new_name for new_name in new_names_split if new_name != ""]
    
    def combine_dates(self,list_of_genres):
        updated_date_genres = []
        for genre_x in list_of_genres:
            if '1939-1945' in genre_x:
                #world war II/20th century for 1939-1945
                updated_date_genres.append('world war ii')
                updated_date_genres.append('20th century')
            elif ('-' in genre_x) and ('1' in genre_x):
                #For date ranges, adds a century tag for both start and end dates in a range
                date_range = re.sub(r'[^0-9-]', '', genre_x)
                txt = date_range.split('-')
                if txt and txt[0].isdigit():
                    start_year = int(txt[0])   
                    updated_date_genres.append(self.get_century_tag(start_year))
                    if txt and txt[1].isdigit():
                        #only add a second century tag if the end date is in a different century than the start date
                        end_year = int(txt[1])
                        if (self.get_century_tag(start_year)) != (self.get_century_tag(end_year)):
                            updated_date_genres.append(self.get_century_tag(end_year))

            elif('1'in genre_x and not '-' in genre_x):
                #For single years (rather than date ranges)
                date = re.sub(r'\D', '', genre_x)
                if date.isdigit:
                    date =int(date)
                    updated_date_genres.append(self.get_century_tag(date))
            else:
                updated_date_genres.append(genre_x)
        return updated_date_genres

    def get_century_tag(self,year):
        if 2000 > year >= 1900:
            return '20th century'
        if 1900 > year >= 1800:
            return '19th century'
        if 1800 > year >= 1700:
            return '18th century'
        if 1700 > year >= 1600:
            return '17th century'
        return ''

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
        """ Selects the first isbn from the list of isbns."""
        if len(isbns) > 0:
            return isbns[0]
        else:
            return ""

    def get_filtered_genres(self):
        """ Return a list of all the offical genres the book has or an empty list 
        if the book has no offical genres.
        """
        filtered_genres = []
        for genre in self.genres:
            if genre in self.official_genres:
                    filtered_genres.append(genre)
        return filtered_genres

    def get_title(self):
        """ Using book data dictonary, return title found for the book, 
        or an empty string if no title was found.
        """
        if "title" in list(self.data.keys()):
            return self.data["title"]
        else:
            return ""

    def get_authors(self):
        """ Using book data dictonary, return list of authors found for the book, 
        or an empty list if no authors were found.
        """
        if "authors" in list(self.data.keys()):
            return self.data["authors"]
        else:
            return []

    def get_description(self):
        """ Using book data dictonary, return description found for the book, 
        or an empty string if no description was found.
        """
        if "description" in list(self.data.keys()):
            return self.data["description"]
        else:
            return ""

    def get_publisher(self):
        """ Using book data dictonary, return publisher found for the book, or 
        an empty string if no publisher was found.
        """
        if "publisher" in list(self.data.keys()):
            return self.data["publisher"]
        else:
            return ""

    def get_publication_date(self):
        """ Using book data dictonary, return publication date found for the book, 
        or an empty string if no publication date was found.
        """
        if "publishedDate" in list(self.data.keys()):
            return self.data["publishedDate"]
        else:
            return ""

    def get_cover_link(self):
        """ Using book data dictonary, return the link to the 
        small thumbnail image of the book's cover, or an empty string if no 
        thumnbail was found.
        """
        if "imageLinks" in list(self.data.keys()):
            if "smallThumbnail" in list(self.data["imageLinks"].keys()):
                return self.data["imageLinks"]["smallThumbnail"]
        return ""

    def get_isbn(self):
        """Return the instance variable containing the book's ibsn, will be the 
        first one found in the google books api query.
        """
        return self.isbn

    def get_isbn_list(self):
        """Return the instance variable containing the list of the books's ibsns."""
        return self.isbn_list

    def get_user_input(self):
        """Return the instance variable containing the title the user inputed."""
        return self.user_input

    def get_genres(self):
        """ Return the instance variable containing a list of all genres found 
        for book.
        """
        return self.genres

    def get_no_match_drink(self):
        """ Return the instance variable containing the drink object that will be used if 
        no pairing is found. Must have the keys name, instructions, information.
        """
        return self.no_match_drink

if __name__ == "__main__":
    app.run(port=8000)