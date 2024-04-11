def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_num_letters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    letter_count.sort(reverse=True, key=sort_on)

    for i in range(len(letter_count)):
        print(f"The {letter_count[i]["letter"]} character was found {letter_count[i]["num"]} times")

    print("--- End report ---")
def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_letters(text):
    letter_list = []
    lowered_text = text.lower()
    # go through each character in text
    for character in lowered_text:
        if character.isalpha() and not any(d["letter"] == character for d in letter_list):
            # a-z and there is no existing dictionary for the character, add it
            char_dict = {"letter": character, "num": 1}
            letter_list.append(char_dict)
        elif character.isalpha():
            # dictionary exists
            for i in range(len(letter_list)):
                # look for the correct dictionary to update
                if letter_list[i]["letter"] == character:
                    letter_list[i]["num"] += 1



    return letter_list

def sort_on(dict):
    return dict["num"]
main()