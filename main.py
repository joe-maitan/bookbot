from stats import *

import sys

def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    
    file_path = sys.argv[1]

    print(f"Analyzing book found at {file_path}...")
    text = get_book_text(file_path)
    num_words = word_count(text)
    print(f"----------- Word Count ----------")
    # print(f"{num_words} words found in the document")
    print(f"Found {num_words} total words")
    char_count = character_count(text)
    #print(f"{char_count}")
    print(f"--------- Character Count -------")
    char_count_list = convert_from_dict_to_list(char_count)
    char_count_list.sort(reverse=True, key=sort_by)
    
    for entry in char_count_list:
        curr_char = entry["char"]
        curr_count = entry["count"]

        if curr_char.isalpha():
            print(f"{curr_char}: {curr_count}")
    

if __name__ == "__main__":
    main()