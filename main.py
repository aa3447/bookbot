def main():
    text = ""
    book = input("Enter the book name (Case Sensitive): ")
    char_amount = input("Enter amount of chars to see in report (Interger): ")
    word_amount = input("Enter amount of words to see in report (Interger): ")
    
    # Validate inputs
    if char_amount.isnumeric():
        char_amount = int(char_amount)
        if char_amount <= 0:
            raise ValueError("Char amount must be greater than 0")
    else:
        raise ValueError("Char amount must be an integer")
    if word_amount.isnumeric():
        word_amount = int(word_amount)
        if word_amount <= 0:
            raise ValueError("Word amount must be greater than 0")
    else:    
        raise ValueError("Word amount must be an integer")
    path =  f"books/{book}.txt"
    try:
        text = get_book_text(path)
    except FileNotFoundError:
        print("Book not found!")
   
    report(text,char_amount,word_amount)

# Returns the number of words in the text
def word_count(text):
    words = text.split()
    return len(words)

# Returns a dictionary with the count of each character in the text
def char_count(text):
    letters = {}
    for letter in text:
        letter = letter.lower()
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

# Returns a dictionary with the count of each word in the text
def individual_word_count(text):
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

# Sorts a dictionary by value in descending order
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

# Prints a report with the number of words, the top char_amount most used characters and the top word_amount most used words
def report(text,char_amount=10,word_amount=10):
    words = word_count(text)
    
    chars = sort_dict_by_value(char_count(text))
    if char_amount > len(chars):
        char_amount = len(chars)
    chars_keys = list(chars.keys())[:char_amount]
    
    if word_amount > words:
        word_amount = words
    individual_words_count = sort_dict_by_value(individual_word_count(text))
    individual_words_count_keys = list(individual_words_count.keys())[:word_amount]
    
    print("---- Report ----")
    print(f"This book has {words} words!")
    for word in individual_words_count_keys:
        print(f"Word '{word}' appears {individual_words_count[word]} times")
    for char in chars_keys:
        if char.isalpha():
            print(f"Char '{char}' appears {chars[char]} times")
    print("---- End of Report ----")

def get_book_text(path):
    with open(path) as book:
        return book.read()

main()