import sys

from stats import get_word_count
from stats import count_char
from stats import get_char_sort

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    word_count = get_word_count(text)
    characters = count_char(text)
    
    sorted_char = get_char_sort(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_char:
        char = item["char"]
        count = item["num"]
        print(f"{char}: {count}")
    
    print("============= END ===============")

main()