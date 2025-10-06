from stats import get_num_words
from stats import get_letter_count
from stats import get_sorted_list
import sys

def get_book_text(path):
    with open(path, encoding="utf-8") as book:
        return book.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    text = get_book_text(path)
    word_count = get_num_words(text)
    print(f"Found {word_count} total words")
    letters = get_letter_count(text)
    print(letters)
    sorted = get_sorted_list(letters)
    for item in sorted:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()
