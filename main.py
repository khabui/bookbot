import sys

from stats import get_num_words, count_chars, sort_chars_freq


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")

    # book_path = "books/frankenstein.txt"
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")

    book_contents = get_book_text(book_path)

    print("----------- Word Count ----------")
    num_words = get_num_words(book_contents)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_frequent = sort_chars_freq(count_chars(book_contents))

    for item in char_frequent:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item['num']}")

    print("============= END ===============")


main()
