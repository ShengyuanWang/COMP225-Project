from flask import Flask, request, render_template
from markupsafe import escape
from book_data import get_isbn, get_book_data

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def get_book():
    if request.method == "POST":
        book = escape(request.form.get("book"))
        return display_result(book)
    return render_template("home.html")

def display_result(book):
    try:
        isbn = get_isbn(book)
        data = get_book_data(isbn, filter=True)

        title = book_data_handling(data, "title")
        authors = book_data_handling(data, "authors")
        description =book_data_handling(data, "description")
        genres = book_data_handling(data, "genres")
        date = book_data_handling(data, "publication_date")
        publisher = book_data_handling(data, "publisher")
        cover_link = book_data_handling(data, "cover_thumbnail")

        return render_template("home.html", title=title, isbn=isbn, authors=authors, publisher=publisher, date=date, genres=genres, description=description, cover_link=cover_link)

    except:
        return render_template("home.html", text="Your book title was not valid.")

def book_data_handling(data, data_key):
    if data_key in data.keys():
        data_point = data[data_key]
        if type(data_point) is list:
            return ",".join(data_point)
        else:
            return data_point
    else:
        return ""


if __name__ == "__main__":
    app.run(port=8000)
