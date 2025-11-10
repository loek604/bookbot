import sys
from stats import wordcount, count_chars,dict_to_list, hulpfun 


def main():
    path = path_arg()
    book_text = get_book_text(path) 
    # let op filepath is een string oftewel:
    # een path-like object
    text = book_text 
    num_words = wordcount(text)
    num_chars_dict = count_chars(text)
    listo = dict_to_list(num_chars_dict)
    printnstuff(path, listo, num_words)


def get_book_text(filepath): 
    
    with open(filepath) as f:
        file_contents = f.read()                        
        return file_contents


def printnstuff(path, listo, num_words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print("--------- Character Count -------")

    for ite in range (0, len(listo)):
        naam =  listo[ite]["name"]
        telling = listo[ite]["num"]
        if naam.isalpha():
            print (naam + ":", telling)


def path_arg():
     
    if len (sys.argv) != 2:
        print(
        "Usage: python3 main.py" 
        " <path_to_book>"
        )
        sys.exit(1)
    
    path = sys.argv[1]

    return path


main()


