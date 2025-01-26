def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print(f"This book has {word_count(text)} words!")
    print(f"This book letter count is {letter_count(text)}!")
    #print(text)

def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    letters = {}
    for letter in text:
        if letter.isalpha() or letter.isspace():
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