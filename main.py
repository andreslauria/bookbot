
from stats import get_numbers_of_words
from stats import num_of_characters, sorted_dict
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {args[1]}...")
    
    book_text = get_book_text(args[1])
    freq = num_of_characters(book_text)
    print("----------- Word Count ----------")
    print(f"Found {get_numbers_of_words(book_text)} total words")
    print("--------- Character Count -------")
    sort_list = sorted_dict(freq)
    for dic in sort_list:
        if dic["character"].isalpha():
            print(f"{dic["character"]}: {dic["count"]}")
    print("============ END ============")




main()