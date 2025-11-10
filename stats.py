def wordcount(text):
    wordlist = text.split()
    num_words = len(wordlist)
    return num_words


def count_chars(text):

    char_bib = {}

    for l in text:
        lowl = l.lower()
        if lowl in char_bib:
            char_bib[lowl] += 1
        else:
            char_bib[lowl] =1

    return char_bib


def hulpfun(items):
    return (items["num"])


def dict_to_list(dicto):
    
    listo = []

    for i in dicto:
        d = {}
        d = {"name":i, "num":dicto[i]}
        listo.append(d)
    
    listo.sort(reverse=True, key=hulpfun)
    
    return listo















# Niet helemaal juist, doet geen symbolen
def charcount(text_wuppercases):
    
    char_lib = {}
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z "
    
    lowered_text = text_wuppercases.lower()
    text = lowered_text
    list_alphabet = alphabet.split()
    
    for letter in range (0,25):
        
        current = list_alphabet[letter] 
        sum_current = text.count(current)
        char_lib[current] = sum_current 
    
    return char_lib


