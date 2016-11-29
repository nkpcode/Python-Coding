# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "E:\drive_e\NYU\Computer_Engineering\Python\words.txt"

#WORDLIST_FILENAME = "words.txt"
#WORDLIST_FILENAME = "E:/drive_e/NYU/Computer_Engineering/Python"

#WORDLIST_FILENAME = "/C:/Users/niyan/Desktop"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWord = list(secretWord)
    lettersGuessed = list(lettersGuessed)
    
    length = len(secretWord)
    count = 0

    while (count <= (length - 1)):

        if not(secretWord[count] in lettersGuessed):
            return False
        count = count + 1

    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretWord = list(secretWord)
    lettersGuessed = list(lettersGuessed)
    
    length = len(lettersGuessed)
    length2 = len(secretWord) 
    count = 0
    count2 = 0
    keepword = ""
    i = 0
    
    for i in range(0,length2):
        keepword = keepword + "_" + " "
    
    keepword = list(keepword)

    while (count <= (length - 1)):
        while(count2 <= (length2 - 1)):
            if(lettersGuessed[count] == secretWord[count2]):
                keepword[2 * count2] = secretWord[count2]
            count2 = count2 + 1
        count = count + 1
        count2 = 0
                
    keepword = "".join(keepword)
    return keepword


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    # FILL IN YOUR CODE HERE...
    lettersAvailable = list(string.ascii_lowercase)
    length2 = len(lettersAvailable)
    length = len(lettersGuessed)
    lettersGuessed = list(lettersGuessed)
    count = 0
    count2 = 0
    
    while(count < length):
        while(count2 < length2):
            if(lettersGuessed[count] == lettersAvailable[count2]):
                lettersAvailable[count2] = ""
            count2 = count2 + 1
        count = count + 1
        count2 = 0
    
    lettersAvailable = "".join(lettersAvailable)
    
    return lettersAvailable

def checkCharAvailable(guessedletter, availableletters):
    """
    Returns True if letter is available to guess
    Returns False if not
    """
        
    if (guessedletter in availableletters):
        return True
    else:
        return False

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    charguess = ""
    singleguess = ""
    availableletters = ""
    guessedSoFar = ""
    guessesLeft = 8 #given in the question
    
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is "+str(len(secretWord))+" letters long."
    print "-------------"

    
    while(guessesLeft >= 0):
        
        print "You have "+str(guessesLeft)+" guesses left."
        
        availableletters = getAvailableLetters(charguess)
        print "Available letters: "+str(availableletters)
        
        singleguess = raw_input("Please guess a letter: ")
        charguess = charguess + singleguess.lower() #keep track of earlier characters entered
        #charguess = charguess.lower() #make lower case the input character
        
        if(checkCharAvailable(singleguess.lower(), availableletters) == False and len(charguess)>1):
            print "Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord, charguess))
            
        else:
            guessedSoFar = getGuessedWord(secretWord, charguess)
            if(checkCharAvailable(singleguess.lower(), secretWord) == True):#if the letter exists in the word
                print "Good guess: "+str(guessedSoFar)
            
            elif(singleguess.lower() != ""):
                print "Oops! That letter is not in my word: "+str(guessedSoFar)
                guessesLeft = guessesLeft - 1
                
                
        print "-------------"
        
        if(guessedSoFar == secretWord):
            print "Congratulations, you won!"
            break
        elif(guessedSoFar != secretWord and guessesLeft == 0):
            print "Sorry, you ran out of guesses. The word was "+str(secretWord)+"."
            break


#hello = hangman(chooseWord(wordlist))
hello = hangman("guanabana")



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)


"""
	Loading word list from file...
	55900 words loaded.
	Welcome to the game, Hangman!
	I am thinking of a word that is 4 letters long.
	-------------
	You have 8 guesses left.
	Available letters: abcdefghijklmnopqrstuvwxyz
	Please guess a letter: a
	Good guess: _ a_ _
	------------
	You have 8 guesses left.
	Available letters: bcdefghijklmnopqrstuvwxyz
	Please guess a letter: a
	Oops! You've already guessed that letter: _ a_ _
	------------
	You have 8 guesses left.
	Available letters: bcdefghijklmnopqrstuvwxyz
	Please guess a letter: s
	Oops! That letter is not in my word: _ a_ _
	------------
	You have 7 guesses left.
	Available letters: bcdefghijklmnopqrtuvwxyz
	Please guess a letter: t
	Good guess: ta_ t
	------------
	You have 7 guesses left.
	Available letters: bcdefghijklmnopqruvwxyz
	Please guess a letter: r
	Oops! That letter is not in my word: ta_ t
	------------
	You have 6 guesses left.
	Available letters: bcdefghijklmnopquvwxyz
	Please guess a letter: m
	Oops! That letter is not in my word: ta_ t
	------------
	You have 5 guesses left.
	Available letters: bcdefghijklnopquvwxyz
	Please guess a letter: c
	Good guess: tact
	------------
	Congratulations, you won!
	
        You have 1 guesses left.
	Available Letters: ijklmnopqrstuvwxyz
	Please guess a letter: i
	Oops! That letter is not in my word: e_ _ e
	-----------
	Sorry, you ran out of guesses. The word was else. 
"""