#Importing time and random functions
import time
import random

#Creating lists/arrays which will store Constants/Vowels/Dictionary. The possible words and longest words of the game.
Constants = []
Vowels = []
Dictionary = []
PossibleWords = []
LongestWords = []

#Generating random letters
def randomGameLettersGenerator():
    randomGameLetters = []
    #Generating 5 constants
    for i in range (0, 5):
        randomGameLetters.append(random.choice(Constants))
    #Generating 4 vowels
    for i in range (0, 4):
        randomGameLetters.append(random.choice(Vowels))
        
    #Returning the list/array of random letters which contain 5 constants and 4 vowels.
    return randomGameLetters

#Method for checking if the word contains random letters
def checker(checkingLetters, word):
    #Set boolean to return at the end.
    isWordGood = False
    #Check for each letter in the random letter list/array.
    for letter in checkingLetters: 
        #Check if that letter is in the word we passed to this method
        if letter in word:
            #If it is, remove it so it's not there anymore and check the rest
            word.remove(letter)
        elif len(word) <= 0:
            #If the none of the random letters are in the word anymore, and the lenght of the word is 0, means the word is good. Return true
            isWordGood = True
        else:
            #Else return false as the word doesn't contain random letters
            isWordGood = False
    return isWordGood

#Method for the "Contestant"
def theGameContestant():
    #Run through each word in list/array Dictionary
    for word in Dictionary:
        #Making sure the word we take has more than 3 letters but less than 9. 
        if len(word) > 3 and len(word) < 9:
            #Passing the random letters and the word as a list to a method checker to see if that word contains random letters.
            if checker(main.gameLetters, list(word)):
                #If checker returns true then add this word POSSIBLE WORDS array
                PossibleWords.append(word)
                #Check if the length of the word is greater than main.LongestWord. If it is, set new longest word length.
                if len(word) > main.LongestWord:
                    main.LongestWord = len(word)
                
#Just a method to read in a file and putting it into list/array rather than hard-coding the lists or repeating the code.
def fileReader(listName,fileName):
    with open(fileName , "r") as f:
        for line in f:
            listName.append(line.rstrip('\n'))
            
def main():
    #Reading in constants, vowels and dictionary from files and puttin them into lists/arrays
    fileReader(Constants, "constants.txt")
    fileReader(Vowels, "vowels.txt")
    fileReader(Dictionary, "dictionary.txt")
    
    #Starting the time and setting the longest word to 0 at the start of the game.
    start_time = time.time()
    main.LongestWord = 0
    
    #Getting the random letters, and shuffling them inside the list/array.
    main.gameLetters = randomGameLettersGenerator()
    random.shuffle(main.gameLetters)
    
    #Let the game begin, the "contestant" figures out which words can be created with the random generated letters (5 constants/4 vowels)
    theGameContestant()
    
    #Loop through each possible word in the array, if the length of the word is greater or the equal to main.LongestWord then add that word to LongestWord array.
    for possibleWord in PossibleWords:
        if len(possibleWord) >= main.LongestWord:
             LongestWords.append(possibleWord)
    
    print("Your random letters are : ", main.gameLetters)
    #for possibleWord in PossibleWords:
     #   if len(possibleWord) >= main.LongestWord:
            #LongestWords.append(possibleWord)
            
    print("Solving...")
    print("Solving...")
    print("Solving...")
    
    StringOfLongestWords = ', '.join(LongestWords)
    
    if len(LongestWords) < 1:
         print("\nThere is not a possible word with the random letters the program has generated.")
    elif len(LongestWords) == 1:
        print("\nThe Longest Possible Word is : " + StringOfLongestWords.title() + ". It contains " + str(main.LongestWord) + " letters.")
    else:
        print("\nThe Longest Possible Words are : " + StringOfLongestWords.title() + ". They contain " + str(main.LongestWord) + " letters.")
        
    print("\nThis game was solved in : %s seconds." %(time.time() - start_time))
    
          
          
main()
    