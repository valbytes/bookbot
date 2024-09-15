import sys



def main(path_to_file):
    with open(path_to_file) as f:
        word_count = 0
        chars = {}
        file_contents = f.read()
        for letter in file_contents:
            if letter.isalpha():
                if letter.lower() in chars:
                    chars[letter.lower()] += 1
                elif letter.lower() not in chars:
                    chars[letter.lower()] = 1
        for word in file_contents.split():    
            word_count += 1
    formatted_chars = convert_dict_to_list_of_dicts(chars)    
    print(f'{path_to_file} contains {word_count} words.')
    print('---- Character Frequency ----')
    for character in formatted_chars:
        print(f"{character['char']} appears in {path_to_file} {character['value']} times.")

def sort_on(dict):
    return dict['value']

def convert_dict_to_list_of_dicts(dict):
    new_list = []
    for key in dict:
        new_list.append({'char': key, 'value': dict[key]})
    new_list.sort(reverse=True, key=sort_on)
    return(new_list)
   

try: 
    main(sys.argv[1])
except IndexError:
        print("Bookbot requires a path input")
except Exception as e:
    print(f"An exception occurred: {e}")