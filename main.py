def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document.")
    count = how_many_chars(text)
    print(count)


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
def how_many_chars(text_string):
    chars = text_string.lower()
    char_count = {}
    for char in chars:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count
def dict_to_list(count):
    new_list = [count]
    print(new_list)

main()