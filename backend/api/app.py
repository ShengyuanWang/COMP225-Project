from flask import Flask, request, render_template
from markupsafe import escape
import json
import random
import requests
from flask_cors import CORS

API_KEY = "AIzaSyAHHByDAWIAvXhTNkajTqazMhBUO045aS0"
GENRES = ["fantasy fiction", "historical fiction", "horror", "thriller", "science fiction",
          "action & adventure", "romance", "mystery fiction"]

app = Flask(__name__)
CORS(app)

@app.route('/', methods =["GET", "POST"])
def get_book():
    """
    Handles user input and displays results
    :returns: renders home.html template
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

@app.route('/test/', methods=["GET"])
def search():
    return Book("Dune").get_pairing_dict()

class Book:
    def __init__ (self, user_input, alchool_data_file="book-alcohol-pairings.json", pairing_file="pairing.json", api_key=API_KEY, official_jsons=GENRES):
        self.user_input = user_input
        self.alchool_data_file = alchool_data_file
        self.pairing_file = pairing_file
        self.api_key = api_key
        self.official_jsons = official_jsons

        self.isbn = self.query_api_isbn(self.user_input)
        self.data = self.query_api_book_data()
        self.genres = self.query_api_genres()

    def get_pairing_dict(self):
        pairing = {}
        pairing["title"] = self.get_title()
        pairing["authors"] = self.get_authors()
        pairing["genres"] = self.get_filtered_genres()
        pairing["cover_link"] = self.get_cover_link()
        pairing["pairing"] = self.get_pairing()
        
        return pairing

    def get_pairing(self, no_match="Bud Light"):
        drinks = self.get_matching_drinks()
        if len(drinks) > 0:
            ran_drink = random.choice(drinks)
            return ran_drink["name"]
        else:
            return no_match

    def get_matching_drinks(self):
        genres = self.get_genres()
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
        except:
            return ""

    def query_api_book_data(self):
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
        filtered_genres = []
        for genre in self.genres:
            if genre in self.official_jsons:
                    filtered_genres.append(genre)
        return filtered_genres

    def get_title(self):
        if "title" in list(self.data.keys()):
            return self.data["title"]
        else:
            return ""

    def get_authors(self):
        if "authors" in list(self.data.keys()):
            return self.data["authors"]
        else:
            return []

    def get_description(self):
        if "description" in list(self.data.keys()):
            return self.data["description"]
        else:
            return ""

    def get_publisher(self):
        if "publisher" in list(self.data.keys()):
            return self.data["publisher"]
        else:
            return ""

    def get_publication_date(self):
        if "publishedDate" in list(self.data.keys()):
            return self.data["publishedDate"]
        else:
            return ""

    def get_cover_link(self):
        if "imageLinks" in list(self.data.keys()):
            if "smallThumbnail" in list(self.data["imageLinks"].keys()):
                return self.data["imageLinks"]["smallThumbnail"]
        return ""

    def get_isbn(self):
        return self.isbn

    def get_user_input(self):
        return self.user_input
    
    def get_pairing_file(self):
        return self.pairing_file

    def get_genres(self):
        return self.genres

if __name__ == "__main__":
    app.run(port=8000)
