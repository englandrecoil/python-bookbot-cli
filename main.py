def get_book_text(path: str) -> str:
    if path == "" or path == None:
        raise Exception("path parameter must be provided!")
    
    with open(path) as f:
        data = f.read()
    return data

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    print(book_text)

main()