import sys
sys.path.append(".")
from app import *

""""Basic unit tests for book class. Does not currently test api queries.
To run tests, cd into backend/api directory and run: pytest tests.
"""

book_valid = Book("dune") 
book_invalid = Book("wqert")

def test_get_pairing_json_obj():
    names_of_drinks = [drink["name"] for drink in book_valid.get_matching_drinks()]
    valid_dict = json.loads(book_valid.get_pairing_json_obj())
    invalid_dict = json.loads(book_invalid.get_pairing_json_obj())
    assert valid_dict["title"] == "Dune"
    assert valid_dict["authors"] == ["Frank Herbert"]
    assert valid_dict["genres"] == ["science fiction"]
    assert valid_dict["cover_link"].startswith("http://books.google.com/books/content?id=ydQiDQAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api")
    assert valid_dict["pairing"] in names_of_drinks
    assert invalid_dict["title"] == ""
    assert invalid_dict["authors"] == []
    assert invalid_dict["genres"] == []
    assert invalid_dict["cover_link"] == ""
    assert invalid_dict["pairing"] == book_invalid.get_no_match_drink()


def test_get_pairing():
    names_of_drinks = [drink["name"] for drink in book_valid.get_matching_drinks()]
    assert book_valid.get_pairing() in names_of_drinks
    assert book_invalid.get_pairing() == book_invalid.get_no_match_drink()
    book_test = Book("sdfght", no_match_drink="red wine")
    assert book_test.get_pairing() == "red wine"

def test_get_matching_drinks():
    valid_book_drinks = book_valid.get_matching_drinks()
    drink_1 = valid_book_drinks[0]
    assert  len(valid_book_drinks) > 0
    assert list(drink_1.keys()) == ["name", "type", "genres"]
    assert type(drink_1["name"]) == str
    assert type(drink_1["type"]) == str
    assert len(drink_1["genres"]) >= 1
    assert book_invalid.get_matching_drinks() == []

def test_get_filtered_genres():
    assert book_valid.get_filtered_genres() == ["science fiction"]
    assert book_invalid.get_filtered_genres() == []

def test_get_title():
    assert book_valid.get_title() == "Dune" 
    assert book_invalid.get_title() == "" 

def test_get_authors():
    assert book_valid.get_authors() == ["Frank Herbert"]
    assert book_invalid.get_authors() == [] 

def test_get_description():
    assert book_valid.get_description().startswith("NOW A MAJOR MOTION PICTURE directed by Denis Villeneuve")
    assert book_invalid.get_description() == ""

def test_get_publisher():
    assert book_valid.get_publisher() == "Penguin" 
    assert book_invalid.get_publisher() == ""  

def test_get_publication_date():
    assert book_valid.get_publication_date() == "2016-10-25" 
    assert book_invalid.get_publication_date() == ""   

def test_get_cover_link():
    assert book_valid.get_cover_link() == "http://books.google.com/books/content?id=ydQiDQAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api" 
    assert book_invalid.get_cover_link() == ""    

def test_get_isbn():
    assert book_valid.get_isbn() == "9780143111580" 
    assert book_invalid.get_isbn() == ""   

def test_get_user_input():
    assert book_valid.get_user_input() == "dune" 
    assert book_invalid.get_user_input() == "wqert"    

def test_get_genres():
    assert "fiction" in book_valid.get_genres()
    assert "dune (imaginary place)" in book_valid.get_genres()
    assert "science fiction" in book_valid.get_genres()
    assert book_invalid.get_genres() == []