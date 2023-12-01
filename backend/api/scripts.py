import json

def collect_all_genres():
    """" Extracts genres and makes json with all of them"""

    with open('book-alcohol-pairings.json') as input_file:
        data = json.load(input_file)

    genre_list = []
    for x in data["alcohols"]:
        genre_list+= x["genres"] + x["key genres"]
    newList = list(set(genre_list))
    
    with open('output.json', 'w') as output_file:
        json.dump(newList, output_file, indent=4)

def transform_json(input_file):
    with open(input_file, 'r') as f:
        original_json = json.load(f)

    transformed_data = {value: key for key, values in original_json.items() for value in values}

    with open("synonyms_lookup.json", 'w') as f:
        json.dump(transformed_data, f, indent=2)

transform_json("synonyms.json")