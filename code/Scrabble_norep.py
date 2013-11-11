#Scrabble_norep.py
#Given the official list of scrabble words returns the letters which aren't
#repeated in any word.
#Author: Gustavo Sinovsky

import urllib
import string

#Alphabet as base comparison
alphabet = string.ascii_uppercase

#Asks whether it should download or not the list of words

b = False
while b is False:
    option = raw_input('Do you have the sowpods.txt file locally? (y/n) ')
    if option == 'y':
        b = True
    elif option == 'n':
        print 'Downloading file...'
        urllib.urlretrieve('http://norvig.com/ngrams/sowpods.txt', 'sowpods.txt')
        print 'File downloaded'
        b = True
    else:
        print 'Not a valid answer'

#Proceeds to open the file and checks for repeated letters in every word
with open('sowpods.txt', 'r') as the_file:
    for word in the_file:
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                    #if the letter is repeated, remove from our alphabet
                    alphabet = alphabet.replace(word[i], "")
print 'The letters are ' + alphabet
the_file.close()
#End of program
