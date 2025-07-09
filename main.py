from stats import *
import sys

def get_book_text(input_path):
    with open(input_path) as f:
        return f.read()

def main():
    if len(sys.argv) == 2:
        print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
        print(f"Found {count_words(get_book_text(sys.argv[1]))} total words")
        print("--------- Character Count -------")
        print_characters_report(get_book_text(sys.argv[1]))
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()