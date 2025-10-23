def get_book_text(path: str) -> str:
    if path == "" or path == None:
        raise Exception("path parameter must be provided!")
    
    try:
        with open(path) as f:
            return f.read()
    except Exception as e:
        raise Exception(e)

def count_book_words(text: str) -> int:
    data = text.split()
    return len(data)

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    words_count = count_book_words(book_text)
    print(f"Found {words_count} total words")

main()