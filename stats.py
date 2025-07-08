

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()

    f.close()
    # print(file_contents)
    return file_contents


def word_count(book_text: str) -> int:
    words = book_text.split()
    return len(words)


def character_count(book_text: str) -> dict:
    character_count = dict()

    words = book_text.split(" ")

    for word in words:
        for i in range(0, len(word)):
            curr_character = word[i].lower()

            if curr_character in character_count:
                character_count[curr_character] += 1
            else:
                character_count[curr_character] = 1

    return character_count


def convert_from_dict_to_list(curr_dictionary: dict) -> list[dict]:
    my_list = []

    for key, value in curr_dictionary.items():
        my_list.append({"char": key, "count": value})

    return my_list


def sort_by(items: dict):
    return items["count"]