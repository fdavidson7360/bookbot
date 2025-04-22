import sys
from stats import get_num_words
from stats import instances_of_characters
from stats import sorted_dict

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_name = sys.argv[1]
    num_words = get_num_words(path_name)
    print(f'{num_words} words found in the document')

    character_dict = instances_of_characters(path_name)
    #print(character_dict)

    returned_dict_list = sorted_dict(character_dict)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path_name}")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in returned_dict_list:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["value"]}')
    print(f"============= END ===============")


main()