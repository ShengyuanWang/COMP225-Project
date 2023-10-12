from flask import Flask, request, render_template
from markupsafe import escape
import json
import random
import requests

API_KEY = "AIzaSyAHHByDAWIAvXhTNkajTqazMhBUO045aS0"
GENRES = ["fantasy fiction", "historical fiction", "horror", "thriller", "science fiction", 
          "action & adventure", "romance", "mystery fiction"] # genres found in json

app = Flask(__name__) 

@app.route('/', methods =["GET", "POST"])
def get_book():
    """
    Handles user input and displays results
    :returns: renders home.html template
    """
    if request.method == "POST":
        book = escape(request.form.get("book"))
        return display_testing(book) # change function to change display
    return render_template("home.html")


@app.route('/test/', methods=["GET"])
def search():
    return "test"

def display_book_data(book):
    """
    Displays all data for a given book
    :param book: escaped book title that the user inputed 
    :returns: renders home.html template
    """
    isbn = get_isbn(book)
    if isbn is not None:
        data = get_book_data(isbn, True)
        if data is not None:
            title = get_data_point(data, "title")
            authors = get_data_point(data, "authors")
            description = get_data_point(data, "description")
            genres = get_data_point(data, "genres")
            date = get_data_point(data, "publication_date")
            publisher = get_data_point(data, "publisher")
            cover_link = get_data_point(data, "cover_thumbnail")
            return render_template("home.html", title=title, isbn=isbn, authors=authors, publisher=publisher,
                                    date=date, genres=genres, description=description, cover_link=cover_link)
        else:
            return render_template("home.html", error=f"No data could be found for your input, {book} (ISBN: {isbn}).")
    else:
        return render_template("home.html", error="Your book title was not valid.")

def display_pairing(book):
    """
    Displays pairing for a given book
    :param book: escaped book title that the user inputed 
    :returns: renders home.html template
    """
    isbn = get_isbn(book)
    if isbn is not None:
        data = get_book_data(isbn, False)
        if data is not None:
            title = get_data_point(data, "title")
            authors = get_data_point(data, "authors")
            list_genres = get_data_point(data, "genres", False)
            filtered_genres = filter_genres(list_genres)
            cover_link = get_data_point(data, "cover_thumbnail")
            drinks = get_matching_drinks(filtered_genres)
            pairing = choose_drink(drinks)
            return render_template("home.html", user_input=book, title=title, isbn=isbn, authors=authors, 
                                cover_link=cover_link, pairing=pairing)
        else:
            return render_template("home.html", error=f"No data could be found for your input, {book} (ISBN: {isbn}).")
    else:
        return render_template("home.html", error=f"The isbn for your input, {book}, could not be found \
                               in the google books API.")

def display_testing(book):
    """
    Function to use for testing which displays information useful for testing, including 
    all book data and pairing data. 
    :param book: escaped book title that the user inputed 
    :returns: renders home.html template
    """
    isbn = get_isbn(book)
    if isbn is not None:
        data = get_book_data(isbn, False)
        if data is not None:
            title = get_data_point(data, "title")
            authors = get_data_point(data, "authors")
            description = get_data_point(data, "description")
            str_genres = get_data_point(data, "genres")
            list_genres = get_data_point(data, "genres", False)
            filtered_genres = filter_genres(list_genres)
            date = get_data_point(data, "publication_date")
            publisher = get_data_point(data, "publisher")
            cover_link = get_data_point(data, "cover_thumbnail")
            drinks = get_matching_drinks(filtered_genres)
            pairing = choose_drink(drinks)
            return render_template("home.html", user_input=book, title=title, isbn=isbn, authors=authors, publisher=publisher, 
                                date=date, genres=str_genres, filtered_genres=filtered_genres, 
                                description=description, cover_link=cover_link, drinks=drinks, 
                                pairing=pairing)
        else:
            return render_template("home.html", error=f"No data could be found for your input, {book} (ISBN: {isbn}).")
    else:
        return render_template("home.html", error=f"The isbn for your input, {book}, could not be found \
                               in the google books API.")


def get_matching_drinks(genres):
    """
    Finds drinks that match a book
    :param genres: List of genres that belong to a book. For best run time, should only include
        genres found in json.
    :returns: List of dictonaries representing drinks that match the genres. drinks will repeat if 
        found more than once. 
    """
    with open("book-alcohol-pairings.json", "r") as f:
        pairings = json.load(f)
    matched_drinks = []        
    if genres is not None and len(genres) > 0:
        for drink in pairings["alcohols"]:
            for genre in genres:
                if genre in drink["genres"]:
                    matched_drinks.append(drink)
    return matched_drinks

def choose_drink(matched_drinks):
    """
    Picks one of the matched drinks to be the pairing.
    :param matched drinks: List of dictonaries representing drinks that match the genres, 
        the output of get_matching_drinks
    :returns: Name of a drink choosen at random, or Bud Light of matched_drinks is an empty list.
    """
    if len(matched_drinks) > 0:
        ran_drink = random.choice(matched_drinks)
        return ran_drink["name"]
    else:
        return "Bud Light"

def get_data_point(data, data_key, join_list=True):
    """
    Gets a data point from the book data dictonary.
    :param data: dictonary representing book data
    :param data_key: string of the key for the data point to be accessed
    :param join_list: flag to join list data points into a comma-separated string
    :returns: data point, or empty string if not found.
    """
    if data_key in data.keys():
        data_point = data[data_key]
        if type(data_point) is list and join_list:
            return ",".join(data_point)
        else:
            return data_point
    else:
        return ""

def filter_genres(unfiltered_genres):
    """
    Filters book's genres to only contain genres found in json.
    :param unfiltered_genres: list all genres found for book
    :returns: list of genres only containg genres found in json, or "no filtered genres" 
        if no genres found.
    """
    filtered_genres = []
    if unfiltered_genres is not None:
        for genre in unfiltered_genres:
            if genre in GENRES:
                filtered_genres.append(genre)
        if len(filtered_genres) > 0:
                return filtered_genres
    return "no filtered genres"

def get_genres(isbn, filter=True):
    """
    Gets genres for a given book using open library API.
    :param isbn: isbn of book
    :param filter: flag to filter genres to only be genres found in json
    :param genres: genres found in json
    :returns: list of genres, or None if no genres found
    """
    base_url = "https://openlibrary.org/api/books"
    params = {
        "bibkeys": f"ISBN:{isbn}",
        "format": "json",
        "jscmd": "data"
    }
    json = requests.get(base_url, params=params).json()

    try:
        data = json.get(f"ISBN:{isbn}", {})
        subjects = data.get('subjects', ['N/A'])
        names = []
        for subject in subjects:
            subjects_split = [word.strip().lower() for word in subject["name"].split(',')]
            for name in subjects_split:
                if filter:
                    if name in GENRES:
                        names.append(name)
                else:
                    names.append(name)

        return list(set(names))

    except:
        return None

def get_book_data(isbn, filter=True, api_key=API_KEY):
    """
    Gets book data for an isbn using google books api. 
    :param isbn: isbn of book
    :param filter: flag to filter book genres to only be genres found in json
    :param api_key: google books api key
    :returns: dictonary with book data, or None if cannot find book data
    """
    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": f"isbn:{isbn}",
        "key": api_key
    }
    data = requests.get(base_url, params=params).json()

    try:
        volume_info = data["items"][0]["volumeInfo"]

        data_dict = {}
        data_dict["isbn"] = isbn
        data_dict["genres"] = get_genres(isbn, filter=filter)

        if "title" in list(volume_info.keys()):
            data_dict["title"] = volume_info["title"]

        if "authors" in list(volume_info.keys()):
            data_dict["authors"] = volume_info["authors"]

        if "description" in list(volume_info.keys()):
            data_dict["description"] = volume_info["description"]

        if "publishedDate" in list(volume_info.keys()):
            data_dict["publication_date"] = volume_info["publishedDate"]

        if "publisher" in list(volume_info.keys()):
            data_dict["publisher"] = volume_info["publisher"]

        if "imageLinks" in list(volume_info.keys()) and "smallThumbnail" in list(volume_info["imageLinks"].keys()):
            data_dict["cover_thumbnail"] = volume_info["imageLinks"]["smallThumbnail"]

        return data_dict

    except:
        return None


def get_isbn(title, api_key=API_KEY):
    """
    Gets isbn for a book using google api.
    :param title: user-inputted title of book
    :param api_key: google books api key
    :returns: isbn of book, or None if no isbn found
    """
    base_url = 'https://www.googleapis.com/books/v1/volumes'
    params = {
        'q': f'intitle:{title}',
        'key': api_key
    }
    try:
        data = requests.get(base_url, params=params).json()['items']
        for entry in data:
            volume_info = entry.get('volumeInfo', {})
            isbn = volume_info.get('industryIdentifiers', [])[0]
            if isbn.get("type") == "ISBN_13":
                return isbn.get("identifier")
    except:
        return None

if __name__ == "__main__":
    app.run(port=8000)
