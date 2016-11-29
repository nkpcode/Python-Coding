

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

print str(getAvailableLetters(""))
