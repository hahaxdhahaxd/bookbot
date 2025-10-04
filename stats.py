def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_characters(char_dict):
    char_list = []
    for char in char_dict:
        char_list.append({"char": char, "num": char_dict[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list