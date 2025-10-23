from stats import *

def main():
    path = "books/frankenstein.txt"

    try:
        book_text = get_book_text(path)
        words_count = count_num_words(book_text)
    except Exception as e:
        print(e)
        return
    
    chars = get_chars_dict(book_text)
    for ch, cnt in chars.items():
        print(f"{repr(ch)}: {cnt}")


main()