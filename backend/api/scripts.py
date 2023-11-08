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

collect_genres()