from flask import Flask, request, render_template
from markupsafe import escape
from book_data import get_isbn, get_book_data, get_genre_list
import json
import random

app = Flask(__name__) 

@app.route('/', methods =["GET", "POST"])
def get_book():
    """
    Handles user input and displays results
    :returns: renders home.html template
    """
    if request.method == "POST":
        book = escape(request.form.get("book"))
        return display_pairing(book) # change function to change display
    return render_template("home.html")

def display_book_data(book):
    """
    Displays all data for a given book
    :param book: escaped book title that the user inputed 
    :returns: renders home.html template
    """
    isbn = get_isbn(book)
    if isbn is not None:
        data = get_book_data(isbn, filter=True)
        title = format_book_data(data, "title")
        authors = format_book_data(data, "authors")
        description = format_book_data(data, "description")
        genres = format_book_data(data, "genres")
        date = format_book_data(data, "publication_date")
        publisher = format_book_data(data, "publisher")
        cover_link = format_book_data(data, "cover_thumbnail")
        return render_template("home.html", title=title, isbn=isbn, authors=authors, publisher=publisher,
                                date=date, genres=genres, description=description, cover_link=cover_link)
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
        data = get_book_data(isbn, filter=True)
        title = format_book_data(data, "title")
        authors = format_book_data(data, "authors")
        genres = format_book_data(data, "genres", False)
        cover_link = format_book_data(data, "cover_thumbnail")
        pairing = choose_drink(get_matching_drinks(genres))
        return render_template("home.html", title=title, authors=authors, pairing=pairing, 
                               cover_link=cover_link)
    else:
        return render_template("home.html", error="Your book title was not valid.")

def display_testing(book):
    """
    Function to use for testing which displays information useful for testing, including 
    all book data and pairing data. 
    :param book: escaped book title that the user inputed 
    :returns: renders home.html template
    """
    isbn = get_isbn(book)
    if isbn is not None:
        data = get_book_data(isbn, filter=False)
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
    if len(genres) > 0:
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
    genre_list = get_genre_list()
    filtered_genres = []
    for genre in unfiltered_genres:
        if genre in genre_list:
            filtered_genres.append(genre)
    if len(filtered_genres) > 0:
        return filtered_genres
    else:
        return "no filtered genres"

if __name__ == "__main__":
    app.run(port=8000)
