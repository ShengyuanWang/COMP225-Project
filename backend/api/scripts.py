import json

def collect_genres():
    """" Extracts genres and makes json with all of them"""

    with open('book-alcohol-pairings.json') as input_file:
        data = json.load(input_file)

    genre_list = []
    for x in data["alcohols"]:
        genre_list+=x["genres"]
        print(x)
    newList =list(set(genre_list))
    
    with open('output.json', 'w') as output_file:
        json.dump(newList, output_file, indent=4)


def collect_key_genres():
    """" Extracts key genres and makes json with all of them"""

    with open('book-alcohol-pairings.json') as input_file:
        key_data = json.load(input_file)

    key_genre_list = []
    for x in key_data["alcohols"]:
        key_genre_list+=x["key genres"]
        print(x)
    newList =list(set(key_genre_list))
    
    with open('key_genres.json', 'w') as output_file:
        json.dump(newList, output_file, indent=4)

collect_genres()
collect_key_genres()