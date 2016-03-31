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
                    LongestWords.append(word)
                
    
def fileReader(listName,fileName):
    with open(fileName , "r") as f:
        for line in f:
            listName.append(line.rstrip('\n'))
            
def main():
    fileReader(Constants, "constants.txt")
    fileReader(Vowels, "vowels.txt")
    fileReader(Dictionary, "dictionary.txt")
    
    start_time = time.time()
    main.LongestWord = 0
    
    main.gameLetters = randomGameLettersGenerator()
    random.shuffle(main.gameLetters)
    theGameContestant()
    
    print("Your random letters are : ", main.gameLetters)
    #for possibleWord in PossibleWords:
     #   if len(possibleWord) >= main.LongestWord:
            #LongestWords.append(possibleWord)
            
    print("Solving...")
    print("Solving...")
    print("Solving...")
    
    StringOfLongestWords = ', '.join(LongestWords)
    
    if len(LongestWords) > 1:
        print("\nThe Longest Possible Words are : " + StringOfLongestWords.title() + ". They contain " + str(main.LongestWord) + " letters.")
    else:
        print("\nThe Longest Possible Word is : " + StringOfLongestWords.title() + ". It contains " + str(main.LongestWord) + " letters.")
        
    print("\nThis game was solved in : %s seconds." %(time.time() - start_time))
    
          
          
main()
    