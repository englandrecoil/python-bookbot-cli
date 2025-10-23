from stats import (
    count_num_words, 
    get_chars_dict, 
    sort_dict,
)
import sys

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path=args[1]
    try:
        book_text = get_book_text(path)
        words_count = count_num_words(book_text)
    except Exception as e:
        print(e)
        return
    
    chars = get_chars_dict(book_text)
    sorted_chars = sort_dict(get_chars_dict(book_text))
    pretty_print(path, words_count, sorted_chars)

def get_book_text(path: str) -> str:
    if path == "" or path == None:
        raise Exception("path parameter must be provided!")
    
    try:
        with open(path) as f:
            return f.read()
    except Exception as e:
        raise Exception(f"couldn't open a file: {e}")

def pretty_print(path, words_count, chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for item in chars:
        if not item["char"].isalpha():
            continue
        print(f'{item["char"]}: {item["num"]}')

    print("============= END ===============")

main()
