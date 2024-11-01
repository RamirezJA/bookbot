def book_quote():
    with open("frankenstein.txt") as f:
        book = f.read()
        return book
def words(book):
    words = book.split()
    num_words = len(words)
    return num_words

def char_num(book):
    char_dict = {}
    for char in book:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def main():
    quote = book_quote()
    word_num = words(quote)
    some_dict = char_num(quote)
    #print(quote)
    #print(word_num)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_num} words found in the document")
    for key,value in some_dict.items():
            print(f"The {key} character was found {value} times")
    print("--- End report ---")
    


    

main()
