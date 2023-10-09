import requests

""" Contains code to query apis and get book data. """

API_KEY = "AIzaSyAHHByDAWIAvXhTNkajTqazMhBUO045aS0"
GENRES = ["fantasy fiction", "historical fiction", "horror", "thriller", "science fiction", 
          "action & adventure", "romance", "mystery fiction"] # genres found in json

def get_genres(isbn, filter=True, genres=GENRES):
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
                    if name in genres:
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
        data = requests.get(base_url, params=params).json()
        first_book =  data['items'][0]
        volume_info = first_book.get('volumeInfo', {})
        return volume_info.get('industryIdentifiers', [])[0].get('identifier')

    except:
        return None

def get_genre_list():
    """ Getter function to get list of genres found in json."""
    return GENRES