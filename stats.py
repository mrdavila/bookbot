def get_word_count(text):
    words = text.split()
    return len(words)

def count_char(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            chars[lowered] = chars.get(lowered, 0) + 1
    return chars

def sort_on(items):
    return items["num"]

def get_char_sort(dict):
    sorted_list = []

    for char, num in dict.items():
        sorted_list.append({"char": char, "num": num})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list