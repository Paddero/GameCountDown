#Importing time and random functions
import time
import random


#Reading the files - words,constants and vowels. Inserting them into arrays.
ListOfWords = open("dictionary.txt","r")
Vowels = open("vowels.txt","r")

#Reading constants from file and saving to a list
with open("constants.txt" , "r") as f:
    Constants = []
    for line in f:
        Constants.append(line.rstrip('\n'))
        
#Reading vowels from file and saving to a list
with open("vowels.txt" , "r") as f:
    Vowels = []
    for line in f:
        Vowels.append(line.rstrip('\n'))

GameWords = []



def main():
    print(Constants)
    print(Vowels)
    

main()
    