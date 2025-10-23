from stats import *

def main():
    path = "books/frankenstein.txt"

    try:
        book_text = get_book_text(path)
        words_count = count_num_words(book_text)
    except Exception as e:
        print(e)
        return
    
    print(f"Found {words_count} total words")

main()