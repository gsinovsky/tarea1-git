#Scrabble_norep.py
#Given the official list of scrabble words returns the letters which aren't
#repeated in any word.
#Author: Gustavo Sinovsky

import urllib
import string
import sys

#Alphabet as base comparison
alphabet = string.ascii_uppercase

#Asks whether it should download or not the list of words
option = raw_input('Do you have the sowpods.txt file locally? (y/n) ')
if option == 'y':
    pass
elif option == 'n':
    print 'Downloading file...'
    urllib.urlretrieve('http://norvig.com/ngrams/sowpods.txt', 'sowpods.txt')
    print 'File downloaded'
else:
    print 'Not a valid answer'
    sys.exit(0)

#Proceeds to open the file and checks for repeated letters in every word
with open('sowpods.txt', 'r') as the_file:
    for word in the_file:
        for pos, letter in enumerate(word):
            if pos < len(word) - 1:
                if letter == word[pos + 1]:
                    #if the letter is repeated, remove from our alphabet
                    alphabet = alphabet.replace(letter, "")
print alphabet
the_file.close()
#End of program
