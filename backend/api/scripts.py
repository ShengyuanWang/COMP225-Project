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

def collect_genre_frequency():
    """" Counts how many times each genre appears in the json"""

    with open('book-alcohol-pairings.json') as input_file:
        data = json.load(input_file)
    genre_freq ={}
    for item in data["alcohols"]:
        genres = item["genres"]
        for element in genres:
            if element in genre_freq.keys():
                genre_freq[element] = genre_freq[element] +1
            else:
                genre_freq[element] = 1
    sorted_genre_freq = sorted(genre_freq.items(), key=lambda x: x[1], reverse=True)

    with open('genre_freq.json', 'w') as output_file:
        json.dump(sorted_genre_freq, output_file, indent=4)
        #for key, value in genre_freq.items():
     #   print("% d : % d" % (key, value))
 
# Driver function
#if __name__ == "__main__":
    #my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
    #for x in data["alcohols"]:
      #  genre_freq+=x["genres"]
     #   print(x)
    #newList =list(set(genre_list))   

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

def collect_genres():
    """" Extracts genres and makes json with all of them"""

    with open('book-alcohol-pairings.json') as input_file:
        data = json.load(input_file)

    genre_list = []
    for x in data["alcohols"]:
        genre_list+= x["genres"]
    newList = list(set(genre_list))
    
    with open('output.json', 'w') as output_file:
        json.dump(newList, output_file, indent=4)

collect_genres()
collect_key_genres()
collect_genre_frequency()