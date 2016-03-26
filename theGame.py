#Importing time and random functions
import time
import random

#Reading the files - words,constants and vowels. Inserting them into arrays.
Constants = []
Vowels = []
Dictionary = []
PossibleWords = []
LongestWords = []

def randomGameLettersGenerator():
    randomGameLetters = []
    for i in range (0, 5):
        randomGameLetters.append(random.choice(Constants))
     
    for i in range (0, 4):
        randomGameLetters.append(random.choice(Vowels))
        
    return randomGameLetters

def checker(checkingLetters, word):
    isWordGood = False
    for letter in checkingLetters:        
        if letter in word:
            word.remove(letter)
        elif len(word) <= 0:
            isWordGood = True
        else:
            isWordGood = False
    return isWordGood

def theGameContestant():
    for word in Dictionary:
        if len(word) > 3:
            if checker(main.gameLetters, list(word)):
                PossibleWords.append(word)
                if len(word) > main.LongestWord:
                    main.LongestWord = len(word)
                
    
def fileReader(listName,fileName):
    with open(fileName , "r") as f:
        for line in f:
            listName.append(line.rstrip('\n'))
            
def main():
    start_time = time.time()
    fileReader(Constants, "constants.txt")
    fileReader(Vowels, "vowels.txt")
    fileReader(Dictionary, "dictionary.txt")
    main.gameLetters = randomGameLettersGenerator()
    main.LongestWord = 0
    theGameContestant()
    print(main.gameLetters)
    for possibleWord in PossibleWords:
        print(possibleWord)
        if len(possibleWord) >= main.LongestWord:
            LongestWords.append(possibleWord)
            
    
    StringOfLongestWords = ', '.join(LongestWords)
    print(LongestWords)
    print("The Longest Possible Words are : " + StringOfLongestWords + ". They contain " + str(main.LongestWord) + " letters.")
    print("This game was solved in : %s" %(time.time() - start_time))
    
          
          
main()
    