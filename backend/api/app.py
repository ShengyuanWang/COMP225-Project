from flask import Flask, request, render_template
from markupsafe import escape
from flask_cors import CORS
from textblob import TextBlob
import json
import requests
import random
import re
import heapq

# DO NOT make this public, keep in private github
API_KEY = "AIzaSyAHHByDAWIAvXhTNkajTqazMhBUO045aS0" 

 # update this when new genres added to alcohol json

with open("all_genres.json") as file:
    jsonData = json.load(file)
GENRES = jsonData


app = Flask(__name__)
CORS(app)

@app.route('/', methods =["GET", "POST"])
def get_book():
    """ Return rendering of home.html template. Handles user input and 
    displays results for testing. 
    """

    if request.method == "POST":
        user_input = escape(request.form.get("book"))
        pairing = Pairing(user_input)
        book = Book(user_input)
        return render_template("home.html", user_input=book.get_user_input(), title=book.get_title(),
                                isbn_list=book.get_isbn_list(), isbn=book.get_isbn(),
                                authors=book.get_authors(), publisher=book.get_publisher(),
                                date=book.get_publication_date(), genres=book.get_genres(),
                                filtered_genres=book.get_filtered_genres(), description=book.get_description(),
                                cover_link=book.get_cover_link(), pairing_json_obj=pairing.get_pairing_json_obj(), 
                                top_matches=[drink["name"] for drink in pairing.get_top_drink_matches(pairing.get_matching_drinks(), book.get_sentiment())],
                                all_matches=pairing.drink_heap_to_ordered_list(pairing.get_matching_drinks()), 
                                pairing=pairing.get_top_pairings()[0],  sentiment=book.get_sentiment())
    return render_template("home.html")

@app.route('/test/<bookname>/<user_types>/<user_allergies>', methods=["GET"])
def search1(bookname, user_types, user_allergies):
    """Return pairing dictonary for testing of frontend intergration."""
    bookname = bookname.replace("%20", " ")
    user_types = user_types.split(",")
    user_allergies = user_allergies.split(",")
    if user_types == ["Nan"]:
        user_types = []
    if user_allergies == ["Nan"]:
        user_allergies = []
    pairing = Pairing(bookname, user_types=user_types, user_allergies=user_allergies)
    return pairing.get_pairing_json_obj()

@app.route('/getAlcohol/<types>', methods=["GET"])
def get_alcohol(types):
    with open('book-alcohol-pairings.json', "r") as f:
        drinks = json.load(f)

    drinks_filtered = []
    for drink in drinks['alcohols']:
        if drink["type"] == types:
            drinks_filtered.append(drink)
    return json.dumps(drinks_filtered)

class Pairing:
    def __init__ (self, user_input, user_allergies=[], user_types=["Beer", "Wine", "Spirits", "Cocktail"], alcohol_data_file="book-alcohol-pairings.json", synonyms_data_file="synonyms_lookup.json",  no_match_drinks="no_match_drinks.json", api_key=API_KEY, official_genres=GENRES):
        """ This class represents a pairing. It passes a json object reprsenting the pairing to the frontend.
        To make the pairing, it creates an instance of the book class in order to be able to get all the book
        data it needs to make an accurate pairing."
        
        Keyword arguments:
        user_input -- string of title inputted by user
        alcohol_data_file -- json dump containing data for alcohol (default "book-alcohol-pairings.json")
        api_key -- string of api key for google api (default API_KEY constant) 
        offical_genres -- list of genres used in alcohol data file (default OFFICAL_GENRES constant) 
        no_match_drink -- string of drink to use if no pairing found (default "Bud Light")
        """
        self.user_allergies = user_allergies
        self.user_types = user_types
        
        with open(alcohol_data_file, "r") as f:
            self.alcohol = json.load(f)
        
        with open(no_match_drinks, "r") as f:
            self.no_match_drinks = json.load(f)

        self.book = Book(user_input, official_genres=official_genres, synonyms_data_file=synonyms_data_file, api_key=api_key)
        self.no_match_found = False
    
    def get_pairing_json_obj(self):
        """ Returns a json object containing book data and pairing for
        use in frontend.
        """
        pairing = {}
        pairing["user_input"] = self.book.get_user_input()
        pairing["title"] = self.book.get_title()
        pairing["authors"] = self.book.get_authors()
        pairing["genres"] = self.book.get_filtered_genres()
        pairing["cover_link"] = self.book.get_cover_link()
        
        top_pairings = self.get_top_pairings()
        pairing_dict = top_pairings[0]
        pairing["name"] = pairing_dict["name"]
        pairing["type"] = pairing_dict["type"]
        pairing["ingredients"] = pairing_dict["ingredients"]
        pairing["instructions"] = pairing_dict["instructions"]
        pairing["image"] = pairing_dict["image"]
        
        if self.no_match_found:
            pairing["notes"] = "We couldn’t find much information for your book, so this match is just our best guess."
        else:
            pairing["notes"] = ""
        
        pairing["rerolls"] = top_pairings[:len(top_pairings)]
        return json.dumps(pairing)

    def get_top_pairings(self):
        """ Return pairing for book. Takes matching drink and 
         returns drink with sentiment score most similar to book. 
        If no matching drinks, returns the drink specfied as the no-match drink.
        """
        all_drinks = self.get_matching_drinks()
        sentiment = self.book.get_sentiment()
        top_pairings = self.get_top_drink_matches(all_drinks, sentiment)
        
        if len(top_pairings) > 0:
            return [self.reduce_drink_dict(pairing) for pairing in top_pairings]
        else:
            self.no_match_found = True
            return [self.reduce_drink_dict(pairing) for pairing in self.get_no_match_drinks()]     
       
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
        book_genres = self.book.get_filtered_genres()
        matched_drinks = []
        heapq.heapify(matched_drinks)

        if book_genres is not None and len(book_genres) > 0:
            for drink in self.alcohol["alcohols"]:
                if drink["type"] in self.user_types:
                    if not any(allergen in drink["allergens"] for allergen in self.user_allergies):
                        shared_genre_count = 0
                        unshared_genre_count = 0
                        for genre in book_genres:
                            if genre in drink["key genres"] :
                                shared_genre_count += 2
                            elif genre in drink["genres"]:
                                shared_genre_count += 1
                            else:
                                unshared_genre_count += .1
                        if shared_genre_count > 0:
                            genre_count = round(shared_genre_count - (unshared_genre_count), 2)
                            heapq.heappush(matched_drinks, DrinkWrapper(drink, genre_count))
        heapq.heapify(matched_drinks)
        return matched_drinks

    def get_no_match_drinks(self):
        """ Return 4 drinks from the no_match_drinks instance variable list"""
        drinks_copy = self.no_match_drinks[:]
        random.shuffle(drinks_copy)
        return drinks_copy[:4]        
    
    def reduce_drink_dict(self, drink_dict, keys=["name", "type", "ingredients", "instructions", "image"]):
        """Takes a drink dict and returns a drink only containing the keys 
        specified """
        return {key: drink_dict[key] for key in keys 
                if key in drink_dict}
    
    def get_top_drink_matches(self, drink_heap, sentiment, range=.2, number_of_matches=4):
        """ Takes the max heap of the drink and returns the drink data dicts that share the 
        highest priority sorted by how much they alisgn .
        """
        top_priority = heapq.nlargest(1, drink_heap)[0].get_priority() if drink_heap else None
        top_matches = []
        for drink_obj in drink_heap:
            if drink_obj.priority >= top_priority - range:
                top_matches.append(drink_obj.get_drink_data())

        heap_list = self.drink_heap_to_ordered_list(drink_heap)
        if len(heap_list) >=  number_of_matches:
            top_matches = [drink_obj.get_drink_data() for drink_obj in heap_list[:number_of_matches]]
        else:
            top_matches = [drink_obj.get_drink_data() for drink_obj in heap_list[:len(heap_list)]]

        return sorted(top_matches, key=lambda drink_match: abs(drink_match["sentiment"] - sentiment))
       

    def drink_heap_to_ordered_list(self, drink_heap):
        """ Turns a heap into an ordered list, where the first element in the list 
        is the entry in the heap with the highest priority."""
        secure_copy = drink_heap[:]
        ordered_list = []
        while secure_copy:
            element = heapq.heappop(secure_copy)
            ordered_list.append(element)
        return ordered_list[::-1]

class Book:
    def __init__ (self, user_input, api_key=API_KEY, official_genres=GENRES, synonyms_data_file="synonyms_lookup.json"):
        """ This class represents a book. Once an object of this class is initiated, that object can be
        used to query book data. 
        
        Keyword arguments:
        user_input -- string of title inputted by user
        alcohol_data_file -- json dump containing data for alcohol (default "book-alcohol-pairings.json")
        api_key -- string of api key for google api (default API_KEY constant) 
        offical_genres -- list of genres used in alcohol data file (default OFFICAL_GENRES constant) 
        no_match_drink -- string of drink to use if no pairing found (default "Bud Light")
        """
        self.user_input = user_input
        self.api_key = api_key

        with open(synonyms_data_file, "r") as f:
            self.synonyms = json.load(f)

        self.no_match_found = False
  
        api_calls = APICalls(user_input, api_key, official_genres, synonyms_data_file)

        self.official_genres = official_genres
        self.isbn_list = api_calls.query_api_isbns()
        self.isbn = api_calls.select_isbn(self.isbn_list)
        self.genres = api_calls.query_api_genres(self.isbn_list)
        self.data = api_calls.query_api_book_data(self.isbn)
    

    def get_filtered_genres(self):
        """ Return a list of all the offical genres the book has or an empty list 
        if the book has no offical genres.
        """
        filtered_genres = []
        for genre in self.genres:
            sub_genre = self.subsitute_genre(genre)
            if sub_genre in self.official_genres:
                    filtered_genres.append(sub_genre)
        return filtered_genres
    
    def subsitute_genre(self, genre):
        if genre in self.synonyms.keys():
            sub = self.synonyms.get(genre)
            return sub
        return genre

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
            print(self.data["imageLinks"])
            if "thumbnail" in list(self.data["imageLinks"].keys()):
                return self.data["imageLinks"]["thumbnail"]
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

class APICalls():
    def __init__(self, user_input, api_key=API_KEY, official_genres=GENRES, synonyms_data_file="synonyms_lookup.json"):
        """This class contains methods that perform API calls to get the data needed to make pairings"""
        self.user_input = user_input 
        self.api_key = api_key
        self.utils = Utils(official_genres, synonyms_data_file)
    
    def query_api_isbns(self):
        """ Gets all isbns for a given book using google book API and user input.
        Assumes the correct title is the first result, and from there, ignoring  
        major stop words and common punctutaion, returns a list of all isbns
        that share the same title as the first result.
        """
        base_url = 'https://www.googleapis.com/books/v1/volumes'
        params = {
            'q': f'intitle:{self.user_input}',
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
                        title = self.utils.filter_title(volume_info["title"])
                        isbns.append(isbn.get("identifier"))
                    if self.utils.filter_title(volume_info["title"]) == title:
                        isbns.append(isbn.get("identifier"))
                    counter += 1
            return isbns
        except:
            return isbns

    def query_api_book_data(self, isbn):
        """ Return a dict of book data, or an empty dictonary 
        if api query fails. Queries google books api using isbn. 
        """
        base_url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": f"isbn:{isbn}",
            "key": self.api_key
        }
        
        if len(isbn) > 0:
            try:
                data = requests.get(base_url, params=params).json()
                return data["items"][0]["volumeInfo"]
            except:
                return {}
        else:
            return {}

    def query_api_genres(self, isbn_list):
        """ Return a list of all genres the book has, or an empty list 
        if api query fails. Queries openlibrary api using isbn. 
        """
        genres = []
        try:            
            for isbn in isbn_list:
                base_url = "https://openlibrary.org/api/books"
                params = {
                    "bibkeys": f"ISBN:{isbn}",
                    "format": "json",
                    "jscmd": "data"
                }
                json = requests.get(base_url, params=params).json()
                data = json.get(f"ISBN:{isbn}", {})
                
                names_split = self.utils.split_subjects(data.get('subjects', ['N/A'])) 
                names_dates_combined = self.utils.combine_dates(names_split)             
                genres += names_dates_combined
            return genres
        except:
            return genres 
        
    def select_isbn(self, isbn_list):
        """ Selects the first isbn from the list of isbns."""
        if len(isbn_list) > 0:
            return isbn_list[0]
        else:
            return ""
  
class Utils():
    def __init__(self, official_genres=GENRES, synonyms_data_file="synonyms_lookup.json"):
        """ This class contains useful util methods. """
        with open(synonyms_data_file, "r") as f:
            self.synonyms = json.load(f)
        self.official_genres = official_genres

    def filter_title(self, title):
        """ Cleans up titles to not include some common stop words, so that the titles 
        can be more easily matched. Used when looking for genres across all 
        versions of a book.
        """
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
    
    def combine_dates(self, list_of_genres):
        """takes in the list of genres and turns all of the date genres into century genres. Works for single dates and date ranges. 
        Returns the updated list of genres"""
        updated_date_genres = []
        #print('OG list')
        #print(list_of_genres)
        for genre_x in list_of_genres:
            if 'early works to 1800' in genre_x:
                updated_date_genres.append(genre_x)
            elif '1939-1945' in genre_x:
                #'world war ii'/'20th century' for '1939-1945'
                updated_date_genres.append('world war ii')
                updated_date_genres.append('20th century')
                updated_date_genres.append('1940s')
            elif '1929-1939' in genre_x:
                updated_date_genres.append('great depression')
                updated_date_genres.append('20th century')
                updated_date_genres.append('1930s')
            elif '1920-1933' in genre_x:
                updated_date_genres.append('prohibition')
                updated_date_genres.append('20th century')
                updated_date_genres.append('1920s')
            elif '1914-1918' in genre_x:
                #'world war i'/'20th century' for '1914-1918'
                updated_date_genres.append('world war i')
                updated_date_genres.append('20th century')
                updated_date_genres.append('1910s')
            elif ('-' in genre_x) and ('1' in genre_x) and not ('.' in genre_x) and not ('=' in genre_x):
                #For date ranges, adds a century tag for both start and end dates in a range. If both the start and end are in the 
                #same century, the tag is only added once. Same is true for decade tags (20th century only)
                date_range = re.sub(r'[^0-9-]', '', genre_x)
                txt = date_range.split('-')
                if len(txt)>2:          # to help avoid including genres that are just the publication date
                    updated_date_genres.append(genre_x)
                elif txt and txt[0].isdigit():
                    start_year = int(txt[0])   
                    updated_date_genres.append(self.get_century_tag(start_year))
                    updated_date_genres.append(self.get_decade_tag(start_year))
                    if txt and txt[1].isdigit():
                        #only add a second century tag and/or decade tag if the end date is in a different century than the start date
                        end_year = int(txt[1])
                        if (self.get_century_tag(start_year)) != (self.get_century_tag(end_year)):
                            updated_date_genres.append(self.get_century_tag(end_year))
                        #f (self.get_decade_tag(start_year)) != (self.get_decade_tag(end_year)):
                            #updated_date_genres.append(self.get_decade_tag(end_year))
                        
            elif('1'in genre_x and not '-' in genre_x  and not ('=' in genre_x)):
                #For single years (rather than date ranges)
                date = re.sub(r'\D', '', genre_x)
                if date.isdigit:
                    date =int(date)
                    updated_date_genres.append(self.get_century_tag(date))
                    updated_date_genres.append(self.get_decade_tag(date))
            else:
                updated_date_genres.append(genre_x)
        #print('updated list')
        #print(updated_date_genres)
        return updated_date_genres
    
    def get_decade_tag_range(self, start_year, end_year):
        if (1920>start_year>=1910) and (1920>end_year>=1910):
            return '1910s'
        elif (1930>start_year>=1920) and (1930>end_year>=1920):
            return '1920s'
        elif (1940>start_year>=1930) and (1940>end_year>=1930):
            return '1930s'
        elif (1950>start_year>=1940) and (1950>end_year>=1940):
            return '1940s'
        elif (1960>start_year>=1950) and (1960>end_year>=1950):
            return '1950s'
        elif (1970>start_year>=1960) and (1970>end_year>=1960):
            return '1960s'
        else:
            return ''
    
    def get_decade_tag(self, year):
        if 1920>year>=1910:
            return '1910s'
        elif 1930>year>=1920:
            return '1920s'
        elif 1940>year>=1930:
            return '1930s'
        elif 1950>year>=1940:
            return '1940s'
        elif 1960>year>=1950:
            return '1950s'
        elif 1970>year>=1960:
            return '1960s'
        else:
            return ''
    
    def get_century_tag(self, year):
        if 2000 > year >= 1900:
            return '20th century'
        if 1900 > year >= 1800:
            return '19th century'
        if 1800 > year >= 1700:
            return '18th century'
        if 1700 > year >= 1600:
            return '17th century'
        return ''

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
  
if __name__ == "__main__":
    app.run(port=8000)