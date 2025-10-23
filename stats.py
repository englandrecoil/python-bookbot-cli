def count_num_words(text: str) -> int:
    data = text.split()
    return len(data)

def get_chars_dict(text: str) -> dict:
    chars = dict()
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_dict(chars):
    list_of_dicts = []
    for ch, cnt in chars.items():
        list_of_dicts.append({"char":ch, "num":cnt})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def sort_on(items):
    return items["num"]