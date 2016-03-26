#Importing time and random functions
import time
import random

#Reading the files - words,constants and vowels. Inserting them into arrays.
Constants = []
Vowels = []
Dictionary = []
GameWords = []

def randomGameLettersGenerator():
    randomGameLetters = []
    for i in range (0, 5):
        randomGameLetters.append(random.choice(Constants))
     
    
    for i in range (0, 4):
        randomGameLetters.append(random.choice(Vowels))
    
    
    return randomGameLetters
        
    
def fileReader(listName,fileName):
    with open(fileName , "r") as f:
        for line in f:
            listName.append(line.rstrip('\n'))
            
    #print(listName)
    
def main():
    fileReader(Constants, "constants.txt")
    fileReader(Vowels, "vowels.txt")
    fileReader(Dictionary, "dictionary.txt")
    gameLetters = randomGameLettersGenerator()
    #print(Constants)
    #print(Vowels)
    print(gameLetters)
    

main()
    