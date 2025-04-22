def get_num_words(file_path):
    num_words = 0
    with open(file_path) as f:
        file_contents = f.read()
    for i in file_contents.split():
        num_words += 1
    return num_words


def instances_of_characters(file_path):
    #file_contents = ""
    freq = {}
    with open(file_path) as f:
        file_contents = f.read()
    for i in file_contents:
        for c in i.lower().split():
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

    return freq

def sort_on(character_dict):
    return character_dict["value"]


#This function will take in a dictionary and sort the list from greatest to least
def sorted_dict(character_dict):
        reorder_dict = {}
        list_to_sort = []
        new_dict = {}
        for i in character_dict:
            list_to_sort.append({"char": i, "value": character_dict[i]})
        list_to_sort.sort(reverse=True, key=sort_on)
        return list_to_sort

    
        
