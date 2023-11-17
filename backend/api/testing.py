import re
def combine_dates(list_of_genres):
        updated_date_genres = []
        print('old genres')
        print(list_of_genres)
        for genre_x in list_of_genres:
            if '1939-1945' in genre_x:
            #world war II/20th century for 1939-1945
                updated_date_genres.append('world war ii')
                updated_date_genres.append('20th century')
            elif ('-' in genre_x) and ('1' in genre_x):
            #For date ranges, adds a century tag for both start and end dates in a range
                date_range = re.sub(r'[^0-9-]', '', genre_x)
                txt = date_range.split('-')
                if txt and txt[0].isdigit():
                    start_year = int(txt[0])
                    updated_date_genres.append(get_century_tag(start_year))
                if txt and txt[1].isdigit():
                    end_year = int(txt[1])
                    updated_date_genres.append(get_century_tag(end_year))

                
            elif '1' in genre_x and not '-' in genre_x:
            #for single years (rather than ranges)
                year = re.sub(r'[^0-9-]', '', genre_x)
                year = int(year)
                if 2000> year >= 1900:
                    updated_date_genres.append('20th century')
                if 1900> year >= 1800:
                    updated_date_genres.append('19th century')
                if 1800> year >= 1700:
                    updated_date_genres.append('18th century')
                if 1700> year >= 1600:
                    updated_date_genres.append('17th century')
            else:
                updated_date_genres.append(genre_x)
        print('new genres')
        print(updated_date_genres)
        return updated_date_genres

combine_dates(['fantasy fiction', 'school stories', 'fiction', 'fantasy', 'nestlé smarties book prize winner', 'juvenile fiction', 'wizards', 'magic', 'schools', 'spanish language materials', 'magia', 'escuelas', 'ficción juvenil', 'novela fantástica', 'hogwarts school of witchcraft and wizardry ', 'imaginary place', 'harry potter ', 'fictitious character', 'wizards -- juvenile fiction', 'witches', 'hogwarts school of witchcraft and wizardry ', 'imaginary organization', 'magos', 'translations from english', 'chinese fiction', 'orphans', 'aunts', 'uncles', 'cousins', 'determination ', 'personality trait) in children', 'friendship', 'potter', 'harry ', 'fictitious character', 'witches fiction', 'wizards fiction', 'schools fiction', 'england fiction', 'magic -- juvenile fiction', 'hogwarts school of witchcraft and wizardry ', 'imaginary place) -- juvenile fiction', 'schools -- juvenile fiction', 'wizards -- fiction', 'magic -- fiction', 'schools -- fiction', 'england -- juvenile fiction', 'england -- fiction', 'fantasy & magic', 'action & adventure', 'witchcraft', 'harry potter ', 'fictional character', 'engels', 'social themes', 'reading level-grade 11', 'reading level-grade 12', 'schools', 'fiction', 'england', 'fiction', 'potter', 'harry ', 'fictitious character', 'fiction', 'hogwarts school of witchcraft and wizardry ', 'imaginary organization', 'fiction', 'wizards', 'fiction', 'magic', 'fiction', "children's fiction", 'adventure and adventurers', 'fiction', 'english literature', 'fiction', 'fantasy', 'general', 'large type books', 'hermione granger ', 'fictitious character', 'ron weasley ', 'fictitious character', 'latin language materials', "children's stories", 'magiciens', 'romans', 'nouvelles', 'etc. pour la jeunesse', 'nécromancie', 'écoles', 'potter', 'harry ', 'personnage fictif', 'romans', 'nouvelles', 'magie', 'family', 'orphans & foster homes', 'magía', 'novela juvenil', 'juvenile', "children's stories", 'english', 'sieg', 'basilisk', 'das böse', 'das gute', 'internat', 'lebensgefahr', 'lebensrettung', 'list', 'magier', 'jugendbuch', 'kampf', 'schule', 'basilisk ', 'fabeltier', 'junge', 'phönix', 'deutschland grenzschutzkommando mitte schule', 'deutschland', 'friendship', 'fiction', 'hogwartes school of witchcraft and wizardry ', 'imaginary place', 'general', 'social issues', 'witches', 'fiction', 'english fantasy literature', 'translations into marathi'])