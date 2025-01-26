def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print(f"This book has {word_count(text)} words!")
    print(f"This book char count is {char_count(text)}!")
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

def get_book_text(path):
    with open(path) as book:
        return book.read()

main()