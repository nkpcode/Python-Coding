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
    
print str(getGuessedWord("apple", ["a","x","a", "a", "a", "p", "a", "a"]))