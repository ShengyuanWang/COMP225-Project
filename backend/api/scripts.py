import json

def update_synonyms_lookup():
    """ Using the synonyms.json file, updates the synonyms_lookup.json file that 
    app.py uses since it is more efficent
    """
    with open("synonyms.json", 'r') as f:
        original_json = json.load(f)

    transformed_data = {value: key for key, values in original_json.items() for value in values}

    with open("synonyms_lookup.json", 'w') as f:
        json.dump(transformed_data, f, indent=2)
    
    with open("../synonyms_lookup.json", 'w') as f:
        json.dump(transformed_data, f, indent=2)
    
def collect_all_genres():
    """" Extracts genres from key_genres and genres and makes json with all of them """
    with open('book-alcohol-pairings.json') as input_file:
        data = json.load(input_file)

    genre_list = []
    for x in data["alcohols"]:
        genre_list+= x["genres"] + x["key_genres"]
    newList = list(set(genre_list))
    
    with open('all_genres.json', 'w') as output_file:
        json.dump(newList, output_file, indent=2)
    
    with open('../all_genres.json', 'w') as output_file:
        json.dump(newList, output_file, indent=2)
    
def collect_genre_frequency():
    """" Counts how many times each genre appears in the json """

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

def collect_key_genres():
    """" Extracts key genres and makes json with all of them"""

    with open('book-alcohol-pairings.json') as input_file:
        key_data = json.load(input_file)

    key_genre_list = []
    for x in key_data["alcohols"]:
        key_genre_list+=x["key_genres"]
        print(x)
    newList =list(set(key_genre_list))
    
    with open('key_genres.json', 'w') as output_file:
        json.dump(newList, output_file, indent=4)

def c():
    """" Extracts genres (not key genres) and makes json with all of them"""

    with open('book-alcohol-pairings.json') as input_file:
        data = json.load(input_file)

    genre_list = []
    for x in data["alcohols"]:
        genre_list+= x["genres"]
    newList = list(set(genre_list))
    
    with open('genres.json', 'w') as output_file:
        json.dump(newList, output_file, indent=4)

def format_lists_json(json_string):
    """ Helper method. Given a json string, returns a json string 
    where the list items are not all on their own line """
    lines = json_string.split("\n")
    fixed_lines = []
    inside = False
    list_container = ""
    for line in lines:
        if inside and "]" in line:
            inside = False
            list_container += line.strip().replace("\n", "")
            fixed_lines.append(list_container)
        elif not inside and "[" in line and "]" not in line and "ingredients" not in line and "alcohols" not in line:
            inside = True
            list_container = line.replace("\n", "")
        elif inside:
            list_container += line.strip().replace("\n", "")
            if len(list_container) > 100:
                fixed_lines.append(list_container)
                list_container = "\t\t\t\t"
        else:
            fixed_lines.append(line)
    return '\n'.join(fixed_lines)

def update_no_match_drinks():
    """ """
    with open('book-alcohol-pairings.json', 'r') as f:
        input_data = json.load(f)
    
    no_match_drinks = []
    for d in input_data["alcohols"]:
        if d["no match drink"] == True:
            no_match_drinks.append(d)
    
    json_string = json.dumps(no_match_drinks, indent=4, separators=(', ', ': '))
    formatted_json = format_lists_json(json_string)
    
    with open('no_match_drinks.json', 'w') as json_file:
        json_file.write(formatted_json)
    
    with open('../no_match_drinks.json', 'w') as json_file:
        json_file.write(formatted_json)

def clean_up_synonyms_in_json():
    """ Using the synonyms.json file, removes synonyms from the json. 
    Updates both alcohol json files. Be careful when using. """
    with open('book-alcohol-pairings.json', 'r') as f:
        input_data = json.load(f)
    
    with open("synonyms.json", 'r') as f:
        synonyms = json.load(f)

    for item in input_data["alcohols"]:
        genres = item["genres"] 
        clean_genres = []
        for genre in genres:
            for key, value in synonyms.items():
                if genre in value:
                    genre = key  # Replace synonym with correct genre name
                    break
            clean_genres.append(genre)
        clean_genres = list(set(clean_genres))
        item["genres"] = clean_genres

    json_string = json.dumps(input_data, indent=4, separators=(', ', ': '))
    formatted_json = format_lists_json(json_string)

    with open('book-alcohol-pairings.json', 'w') as json_file:
        json_file.write(formatted_json)
    
    with open('../book-alcohol-pairings.json', 'w') as json_file:
        json_file.write(formatted_json)

def add_new_key_to_json(key, value):
    """ Adds a new key with default json to all entries. Be careful when using. """
    with open('book-alcohol-pairings.json', 'r') as f:
        input_data = json.load(f)
    
    with open("synonyms.json", 'r') as f:
        synonyms = json.load(f)

    for item in input_data["alcohols"]:
        item[key] = value

    json_string = json.dumps(input_data, indent=4, separators=(', ', ': '))
    formatted_json = format_lists_json(json_string)

    with open('book-alcohol-pairings.json', 'w') as json_file:
        json_file.write(formatted_json)
    
    with open('../book-alcohol-pairings.json', 'w') as json_file:
        json_file.write(formatted_json)

def check_book_alcohol_pairing_json():
    """ This function makes sure that the json drink entries are the same in each file
    and also have all the correct keys.
    """
    with open('book-alcohol-pairings.json', 'r') as f:
        input_data1 = json.load(f)
    
    with open('book-alcohol-pairings.json', 'r') as f:
        input_data2 = json.load(f)
    
    for entry1, entry2 in zip(input_data1["alcohols"], input_data2["alcohols"]):
        if entry1 != entry2:
            raise ValueError(f"There is a difference in the two json files.")

        entry_keys = list(entry1.keys())
        if entry_keys != ['name', 'type', 'key_genres', 'genres', 'sentiment', 'ingredients', 'instructions', 'allergens', 'image', 'no match drink','description']:
                if "name" in entry_keys:
                    name = entry1["name"]
                else:
                    name = "[name missing]"
                
                raise ValueError(f"There is a key missing in {name}, it has these keys: {entry_keys}")

    print("Sucess!")

# run to update data files
collect_genre_frequency()
collect_key_genres()
collect_all_genres()
update_no_match_drinks() 
update_synonyms_lookup()
check_book_alcohol_pairing_json()
