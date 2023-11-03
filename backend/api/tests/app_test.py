import sys
sys.path.append(".")
from app import *

""""Basic unit tests for book class. Does not currently test api queries.
To run tests, cd into backend/api directory and run: pytest tests.
"""

book_valid = Book("Dune") 
book_invalid = Book("wqert")
book_multiversion = Book("Pride and Prejudice")

def test_get_pairing_json_obj():
    names_of_drinks = [drink["name"] for drink in book_valid.get_matching_drinks()]
    valid_dict = json.loads(book_valid.get_pairing_json_obj())
    invalid_dict = json.loads(book_invalid.get_pairing_json_obj())
    assert list(valid_dict.keys()) == ["title", "authors", "genres", "cover_link", "name", "instructions", "information"]
    assert type(valid_dict["instructions"]) is list 
    assert type(valid_dict["information"]) is str 
    assert type(valid_dict["name"]) is str 
    assert valid_dict["title"] == "Dune"
    assert valid_dict["authors"] == ["Frank Herbert"]
    assert list(set(valid_dict["genres"])) == ["science fiction"]
    assert valid_dict["cover_link"].startswith("http://books.google.com/books/content?id=ydQiDQAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api")
    assert valid_dict["name"] in names_of_drinks
    assert list(invalid_dict.keys()) == ["title", "authors", "genres", "cover_link", "name", "instructions", "information"]
    assert invalid_dict["title"] == ""
    assert invalid_dict["authors"] == []
    assert invalid_dict["genres"] == []
    assert invalid_dict["cover_link"] == ""
    assert invalid_dict["name"] == book_invalid.get_no_match_drink()["name"]
    assert invalid_dict["instructions"] == book_invalid.get_no_match_drink()["instructions"]
    assert invalid_dict["information"] == book_invalid.get_no_match_drink()["information"]

def test_get_pairing():
    names_of_drinks = [drink["name"] for drink in book_valid.get_matching_drinks()]
    assert book_valid.get_pairing()["name"] in names_of_drinks
    assert book_invalid.get_pairing() == book_invalid.get_no_match_drink()

def test_get_matching_drinks():
    valid_book_drinks = book_valid.get_matching_drinks()
    drink_1 = valid_book_drinks[0]
    assert  len(valid_book_drinks) > 0
    assert list(drink_1.keys()) == ["name", "type", "genres", "instructions", "information"]
    assert type(drink_1["name"]) == str
    assert type(drink_1["type"]) == str
    assert len(drink_1["genres"]) >= 1
    assert book_invalid.get_matching_drinks() == []

def test_split_subjects():
    assert book_valid.split_subjects([]) == []
    assert book_valid.split_subjects([{"name":"a"}]) == ["a"]
    assert book_valid.split_subjects([{"name":"-"}]) == []
    assert book_valid.split_subjects([{"name":"()"}]) == []
    assert book_valid.split_subjects([{"name":"a"}, {"name":"b"}]) == ["a","b"]
    assert book_valid.split_subjects([{"name":"Abc"}, {"name":"BbBB"}]) == ["abc","bbbb"]
    assert book_valid.split_subjects([{"name":"aa   "}, {"name":"   bb"}]) == ["aa","bb"]
    assert book_valid.split_subjects([{"name":"aa-bb"}, {"name":"cc"}]) == ["aa","bb", "cc"]
    assert book_valid.split_subjects([{"name":"aa—-bb"}, {"name":"cc"}]) == ["aa","bb", "cc"]
    assert book_valid.split_subjects([{"name":"aa(bb)"}, {"name":"cc"}]) == ["aa","bb", "cc"]
    assert book_valid.split_subjects([{"name":"(aa)"}]) == ["aa"]

def test_filter_title():
    assert book_valid.filter_title("heLLo and WORLD!") == "heLLo WORLD!"
    assert book_valid.filter_title("and a the") == ""
    assert book_valid.filter_title("and ?!,") == "?!,"
    assert book_valid.filter_title("hello world    ") == "hello world"
    assert book_valid.filter_title("the hello") == "hello"

def test_select_isbn():
    assert book_valid.select_isbn(book_valid.get_isbn_list()) == "9780143111580"
    assert book_invalid.select_isbn(book_invalid.get_isbn_list()) == ""

def test_get_filtered_genres():
    assert list(set(book_valid.get_filtered_genres())) == ["science fiction"]
    assert book_invalid.get_filtered_genres() == []

def test_get_title():
    assert book_valid.get_title() == "Dune" 
    assert book_invalid.get_title() == "" 

def test_get_authors():
    assert book_valid.get_authors() == ["Frank Herbert"]
    assert book_invalid.get_authors() == [] 

def test_get_description():
    assert book_valid.get_description().startswith("NOW A MAJOR MOTION PICTURE")
    assert book_invalid.get_description() == ""

def test_get_publisher():
    assert book_valid.get_publisher() == "Penguin" 
    assert book_invalid.get_publisher() == ""  

def test_get_publication_date():
    assert book_valid.get_publication_date() == "2016-10-25" 
    assert book_invalid.get_publication_date() == ""   

def test_get_cover_link():
    assert book_valid.get_cover_link().startswith("http://books.google.com/books/content?id=")

def test_get_isbn():
    assert book_valid.get_isbn() == "9780143111580" 
    assert book_invalid.get_isbn() == ""   
    assert book_multiversion.get_isbn() == "9789390504640"

def test_get_isbn_list():
    assert book_valid.get_isbn_list() ==  ["9780143111580", "9780143111580", "9780593099322"]
    assert book_invalid.get_isbn_list() == []  
    assert len(book_multiversion.get_isbn_list()) >= 4

def test_get_user_input():
    assert book_valid.get_user_input() == "Dune" 
    assert book_invalid.get_user_input() == "wqert"    

def test_get_genres():
    assert "fiction" in book_valid.get_genres()
    assert "imaginary place" in book_valid.get_genres()
    assert "science fiction" in book_valid.get_genres()
    assert book_invalid.get_genres() == []
    assert "women in england" in book_multiversion.get_genres()
    assert "brothers and sisters" in book_multiversion.get_genres()

def test_get_no_matching_drinks():
    no_match = Book("wqertvfghj", no_match_drink={"name":"water", "instructions":["no"], "information":"none"})
    assert no_match.get_no_match_drink()["name"] == "water"
    assert no_match.get_no_match_drink()["instructions"] == ["no"]
    assert no_match.get_no_match_drink()["information"] == "none"

