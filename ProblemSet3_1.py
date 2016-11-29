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
    
print isWordGuessed('grapefruit', ['q', 'g', 'i', 'r', 's', 'c', 'p', 'f', 'v', 'o'])