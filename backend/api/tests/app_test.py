import sys
sys.path.append(".")
from app import *

""" Unit tests for book class. 
To run tests, cd into backend/api directory and run: pytest tests.
"""

book_valid = Book("Dune") 
book_invalid = Book("wqert")
book_multiversion = Book("Pride and Prejudice")

def test_get_pairing_json_obj():
    valid_dict = json.loads(book_valid.get_pairing_json_obj())
    assert type(valid_dict["title"]) is str 
    assert type(valid_dict["authors"]) is list 
    assert type(valid_dict["genres"]) is list 
    assert type(valid_dict["cover_link"]) is str 
    assert type(valid_dict["name"]) is str 
    assert type(valid_dict["type"]) is str 
    assert type(valid_dict["ingredients"]) is list 
    assert type(valid_dict["instructions"]) is str 
    assert valid_dict["title"] == "Dune"
    assert valid_dict["authors"] == ["Frank Herbert"]
    assert set(valid_dict["genres"]) == set(["science-fiction", "science fiction"])
    assert valid_dict["cover_link"].startswith("http://books.google.com/books/content?id")
    assert valid_dict["name"] in [drink.get_drink_data()["name"] for drink in book_valid.get_matching_drinks()]
    assert valid_dict["ingredients"] in [drink.get_drink_data()["ingredients"] for drink in book_valid.get_matching_drinks()]
    assert valid_dict["instructions"] in [drink.get_drink_data()["instructions"] for drink in book_valid.get_matching_drinks()]

    invalid_dict = json.loads(book_invalid.get_pairing_json_obj())
    assert type(invalid_dict["title"]) is str 
    assert type(invalid_dict["authors"]) is list 
    assert type(invalid_dict["genres"]) is list 
    assert type(invalid_dict["cover_link"]) is str 
    assert type(invalid_dict["name"]) is str 
    assert type(invalid_dict["type"]) is str 
    assert type(invalid_dict["ingredients"]) is list 
    assert type(invalid_dict["instructions"]) is str 
    assert invalid_dict["title"] == ""
    assert invalid_dict["authors"] == []
    assert invalid_dict["genres"] == []
    assert invalid_dict["cover_link"] == ""
    assert invalid_dict["name"] == book_invalid.get_no_match_drink()["name"]
    assert invalid_dict["ingredients"] == book_invalid.get_no_match_drink()["ingredients"]
    assert invalid_dict["instructions"] == book_invalid.get_no_match_drink()["instructions"]

def test_get_pairing():
    valid_pairing = book_valid.get_top_pairings()[0]
    assert type(valid_pairing["name"]) is str
    assert type(valid_pairing["type"]) is str
    assert type(valid_pairing["ingredients"]) is list
    assert type(valid_pairing["instructions"]) is str
    assert valid_pairing["name"] in [drink["name"] for drink in book_valid.get_top_drink_matches(book_valid.get_matching_drinks(), book_valid.get_sentiment())]
    assert valid_pairing["name"] in [drink.get_drink_data()["name"] for drink in book_valid.get_matching_drinks()]
    assert valid_pairing["type"].lower() in ["beer", "wine", "cocktails", "spirits"]
    assert valid_pairing["ingredients"] in [drink.get_drink_data()["ingredients"] for drink in book_valid.get_matching_drinks()]
    assert valid_pairing["instructions"] in [drink.get_drink_data()["instructions"] for drink in book_valid.get_matching_drinks()]

    invalid_pairings = book_invalid.get_top_pairings()
    assert len(invalid_pairings) == 4
    invalid_pairing = invalid_pairings[0]
    assert type(invalid_pairing["name"]) is str
    assert type(invalid_pairing["type"]) is str
    assert type(invalid_pairing["ingredients"]) is list
    assert type(invalid_pairing["instructions"]) is str
    assert invalid_pairing["name"] == book_invalid.get_no_match_drink()["name"]
    assert invalid_pairing["ingredients"] == book_invalid.get_no_match_drink()["ingredients"]
    assert invalid_pairing["instructions"] == book_invalid.get_no_match_drink()["instructions"]

def test_get_matching_drinks():
    valid_book_drinks = book_valid.get_matching_drinks()
    drink_1 = valid_book_drinks[0].get_drink_data()
    assert len(book_multiversion.get_matching_drinks()) >= 3
    assert len(valid_book_drinks) >= 3
    assert list(drink_1.keys()) == ["name", "type", "genres", "sentiment", "ingredients", "instructions", "allergens"]
    assert type(drink_1["name"]) is str
    assert type(drink_1["type"]) is str
    assert type(drink_1["genres"])is list
    assert type(drink_1["ingredients"]) is list
    assert type(drink_1["instructions"])is str
    assert book_invalid.get_matching_drinks() == []
    
    # testing allergy feature
    book_allergy = Book("On Great Fields", ["gluten"]) 
    book_no_allergy = Book("On Great Fields") 
    assert book_allergy.get_top_pairings()[0]["type"] in ["Cocktail", "Wine", "Spirits"]
    assert book_no_allergy.get_top_pairings()[0]["name"] == "Porter"

    # testing drink type feature
    book_beer_only = Book("Dune", [], ["beer"]) 
    assert book_beer_only.get_top_pairings()[0]["type"]  == "Beer"

def test_get_top_drink_matches():
    drink1_heap = book_valid.get_matching_drinks()
    sentiment = book_valid.get_sentiment()
    assert len(book_valid.get_top_drink_matches(drink1_heap, sentiment)) >= 3
    assert type(book_valid.get_top_drink_matches(drink1_heap, sentiment)) is list 
    assert [type(ele) is dict for ele in book_valid.get_top_drink_matches(drink1_heap, sentiment)]
    drink2_heap = book_invalid.get_matching_drinks()
    assert len(book_invalid.get_top_drink_matches(drink2_heap, sentiment)) == 0
    assert type(book_invalid.get_top_drink_matches(drink2_heap, sentiment)) is list 

def test_drink_heap_to_ordered_list():
    drink_heap = book_valid.get_matching_drinks()
    ordered_list = book_valid.drink_heap_to_ordered_list(drink_heap)
    assert len(drink_heap) == len(ordered_list)
    assert type(ordered_list) == list 
    assert ordered_list[0].get_priority() > ordered_list[len(ordered_list)-1].get_priority()

def test_get_sentiment():
    assert book_invalid.get_sentiment() == 0
    score = book_valid.get_sentiment()
    assert type(score) is float 
    assert len(str(score).split('.')[1]) if '.' in str(score) else 0 == 2
    assert score < .5 
    assert score > .0

def test_query_api_isbn():
    assert type(book_valid.query_api_isbns(book_valid.get_user_input())) is list 
    assert type(book_invalid.query_api_isbns(book_invalid.get_user_input())) is list 
    assert type(book_multiversion.query_api_isbns(book_multiversion.get_user_input())) is list 
    assert len(book_valid.query_api_isbns(book_valid.get_user_input())) > 2
    assert len(book_invalid.query_api_isbns(book_invalid.get_user_input())) == 0
    assert "9780143111580" in book_valid.query_api_isbns(book_valid.get_user_input())

def test_query_api_book_data():
    assert book_invalid.query_api_book_data() == {}
    data_dict = book_valid.query_api_book_data()
    assert type(data_dict) is dict 
    assert "title" in data_dict.keys()
    assert type(data_dict["title"]) is str
    assert data_dict["title"] == "Dune" 
    assert "authors" in data_dict.keys()
    assert type(data_dict["authors"]) is list
    assert data_dict["authors"] ==  ["Frank Herbert"]
    assert "description" in data_dict.keys()
    assert type(data_dict["description"]) is str
    assert data_dict["description"].startswith("NOW A MAJOR MOTION PICTURE")    
    assert "publisher" in data_dict.keys()
    assert type(data_dict["publisher"]) is str
    assert data_dict["publisher"] == "Penguin" 
    assert "publishedDate" in data_dict.keys()
    assert type(data_dict["publishedDate"]) is str
    assert data_dict["publishedDate"] == "2016-10-25" 
    assert "imageLinks" in data_dict.keys()
    assert "smallThumbnail" in data_dict["imageLinks"].keys()
    assert type(data_dict["imageLinks"]["smallThumbnail"]) is str
    assert data_dict["imageLinks"]["smallThumbnail"].startswith("http://books.google.com/books/content?id=")

def test_query_api_genres():
    assert book_invalid.query_api_genres() == []
    genres_list = book_valid.query_api_genres()
    assert type(genres_list) is list 
    assert "science fiction" in genres_list
   
def test_split_subjects():
    assert book_valid.split_subjects([]) == []
    assert book_valid.split_subjects([{"name":"a"}]) == ["a"]
    assert book_valid.split_subjects([{"name":"()"}]) == []
    assert book_valid.split_subjects([{"name":"a"}, {"name":"b"}]) == ["a","b"]
    assert book_valid.split_subjects([{"name":"Abc"}, {"name":"BbBB"}]) == ["abc","bbbb"]
    assert book_valid.split_subjects([{"name":"aa   "}, {"name":"   bb"}]) == ["aa","bb"]
    assert book_valid.split_subjects([{"name":"aa-bb"}, {"name":"cc"}]) == ["aa-bb","cc"]
    assert book_valid.split_subjects([{"name":"aa—–bb"}, {"name":"cc"}]) == ["aa","bb", "cc"]
    assert book_valid.split_subjects([{"name":"aa—–bb-dd"}, {"name":"cc"}]) == ["aa","bb-dd", "cc"]
    assert book_valid.split_subjects([{"name":"aa/bb"}, {"name":"cc"}]) == ["aa","bb", "cc"]
    assert book_valid.split_subjects([{"name":"aa(bb)"}, {"name":"cc"}]) == ["aa","bb", "cc"]
    assert book_valid.split_subjects([{"name":"(aa)"}]) == ["aa"]

def test_get_sentiment():
    assert len(str(book_valid.get_sentiment())) <= 4
    assert book_valid.get_sentiment() >= -1 and book_valid.get_sentiment() <= 1
    assert book_invalid.get_sentiment() == 0

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
    assert set(book_valid.get_filtered_genres()) == set(["science-fiction", "science fiction"])
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
    assert book_multiversion.get_isbn() in book_multiversion.get_isbn_list()

def test_get_isbn_list():
    assert book_valid.get_isbn_list() ==  ["9780143111580", "9780143111580", "9780593099322"]
    assert book_invalid.get_isbn_list() == []  

def test_get_user_input():
    assert book_valid.get_user_input() == "Dune" 
    assert book_invalid.get_user_input() == "wqert"    

def test_get_genres():
    assert "fiction" in book_valid.get_genres()
    assert "imaginary place" in book_valid.get_genres()
    assert "science-fiction" in book_valid.get_genres()
    assert book_invalid.get_genres() == []
    assert "women in england" in book_multiversion.get_genres()
    assert "brothers and sisters" in book_multiversion.get_genres()

def test_get_no_matching_drinks():
    no_match = Book("wqertvfghj", no_match_drink={"name":"water", "instructions":["no"], "information":"none"})
    assert no_match.get_no_match_drink()["name"] == "water"
    assert no_match.get_no_match_drink()["instructions"] == ["no"]
    assert no_match.get_no_match_drink()["information"] == "none"

