def main():
    with open("books/frankenstein.txt") as book:
        text = book.read()
    print(text)

main()