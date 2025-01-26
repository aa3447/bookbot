def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print(word_count(text))
    #print(text)

def word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as book:
        return book.read()

main()