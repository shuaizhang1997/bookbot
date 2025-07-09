def count_words(text):
    words = text.split()
    return len(words)

def print_characters_report(text):
    chars = text.lower()
    char_count = {}
    for char in chars:
        char_count[char] = char_count.get(char, 0) + 1
    sorted_items = list(char_count.items())
    sorted_items.sort()
    for char, count in sorted_items:
        print(f"{char}: {count}")