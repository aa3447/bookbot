def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    report(text)
    #print(text)

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    letters = {}
    for letter in text:
        letter = letter.lower()
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

def report(text):
    words = word_count(text)
    chars = sort_dict_by_value(char_count(text))
    print("---- Report ----")
    print(f"This book has {words} words!")
    for char in chars:
        if char.isalpha():
            print(f"Char '{char}' appears {chars[char]} times")
    print("---- End of Report ----")

def get_book_text(path):
    with open(path) as book:
        return book.read()

main()