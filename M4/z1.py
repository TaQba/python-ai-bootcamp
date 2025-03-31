check_words = ['kajak', 'potop', 'papa']

def palindrom(word):
    rev_word = ''
    for i in range(len(word)-1, -1, -1):
        rev_word += word[i]
    return word == rev_word

for word in check_words:
    print("{}:\t {}".format (word, palindrom(word)))
