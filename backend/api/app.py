from flask import Flask, request, render_template
from markupsafe import escape
import json
import random
import requests
from flask_cors import CORS

# DO NOT make this public, keep in private github
API_KEY = "AIzaSyAHHByDAWIAvXhTNkajTqazMhBUO045aS0" 

 # update this when new genres added to alcohol json
GENRES = ["fantasy fiction", "historical fiction", "horror", "thriller", "science fiction",
          "action & adventure", "romance", "mystery fiction"]

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
        return render_template("home.html", user_input=book.get_user_input(), title=book.get_title(), isbn=book.get_isbn(),
                        authors=book.get_authors(), publisher=book.get_publisher(),
                        date=book.get_publication_date(), genres=book.get_genres(),
                        filtered_genres=book.get_filtered_genres(), description=book.get_description(),
                        cover_link=book.get_cover_link(), drinks=book.get_matching_drinks(),
                        pairing=book.get_pairing())
    return render_template("home.html")

@app.route('/test/<bookname>', methods=["GET"])
def search1(bookname):
    """Return pairing dictonary for testing of frontend intergration."""
    book = Book(bookname)
    return book.get_pairing_json_obj()


class Book:
    def __init__ (self, user_input, alchool_data_file="book-alcohol-pairings.json", api_key=API_KEY, official_genres=GENRES, no_match_drink="Bud Light"):
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
        self.alchool_data_file = alchool_data_file
        self.api_key = api_key
        self.official_genres = official_genres
        self.no_match_drink = no_match_drink

        self.isbn = self.query_api_isbn(self.user_input)
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
        pairing["pairing"] = self.get_pairing()
        
        return json.dumps(pairing)

    def get_pairing(self):
        """ Return pairing for book. Takes matching drink and 
        randomly returns one drink as the pairing. If no drink is found,
        returns the drink specfied as the no-match drink.
        """
        drinks = self.get_matching_drinks()
        if len(drinks) > 0:
            ran_drink = random.choice(drinks)
            return ran_drink['name']
        else:
            return self.no_match_drink

    def get_matching_drinks(self):
        """ Return list of drinks that match book based on data in json file. 
        If no drinks match, returns an empty list. Drinks are represented as
        dictonaries. 
        """
        genres = self.get_filtered_genres()
        with open(self.alchool_data_file, "r") as f:
            pairings = json.load(f)
        matched_drinks = []

        if genres is not None and len(genres) > 0:
            for drink in pairings["alcohols"]:
                for genre in genres:
                    if genre in drink["genres"]:
                        matched_drinks.append(drink)
        return matched_drinks

    def query_api_isbn(self, title):
        """Return isbn of book as a string, or an empty string 
        if api query fails. Queries google books api using user inputted title.
        Will return first isbn found for book that is in the ISBN_13 format.
        
        Keyword arguments:
        title -- book title inputted by user
        """
        base_url = 'https://www.googleapis.com/books/v1/volumes'
        params = {
            'q': f'intitle:{title}',
            'key': self.api_key
        }

        try:
            data = requests.get(base_url, params=params).json()['items']
            for entry in data:
                volume_info = entry.get('volumeInfo', {})
                isbn = volume_info.get('industryIdentifiers', [])[0]
                if isbn.get("type") == "ISBN_13":
                    return isbn.get("identifier")
            return ""
        except:
            return ""

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
        base_url = "https://openlibrary.org/api/books"
        params = {
            "bibkeys": f"ISBN:{self.isbn}",
            "format": "json",
            "jscmd": "data"
        }

        try:
            json = requests.get(base_url, params=params).json()
            data = json.get(f"ISBN:{self.isbn}", {})
            subjects = data.get('subjects', ['N/A'])
            names = []
            for subject in subjects:
                subjects_split = [word.strip().lower() for word in subject["name"].split(',')]
                for name in subjects_split:
                    names.append(name)
            return list(set(names))
        except:
            return []

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
        """Return the instance variable containing the book's ibsn."""
        return self.isbn

    def get_user_input(self):
        """Return the instance variable containing the title the user inputed."""
        return self.user_input

    def get_genres(self):
        """Return the instance variable containing a list of all genres found 
        for book.
        """
        return self.genres

    def get_no_match_drink(self):
        """Return the instance variable containingthe drink that will be used if 
        no pairing is found.
        """
        return self.no_match_drink

if __name__ == "__main__":
    app.run(port=8000)
