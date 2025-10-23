def get_book_text(path: str) -> str:
    if path == "" or path == None:
        raise Exception("path parameter must be provided!")
    
    try:
        with open(path) as f:
            return f.read()
    except Exception as e:
        raise Exception(f"couldn't open a file: {e}")

def count_num_words(text: str) -> int:
    data = text.split()
    return len(data)

