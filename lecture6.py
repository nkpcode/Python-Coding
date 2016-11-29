def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    flag = 0
    newTup = ()
    counter = 0
    
    for i in aTup:
        counter = counter + 1
        
        if (counter % 2 != 0):
            newTup = newTup + (i,)
            
    return newTup
    
print oddTuples((1,2,3,4,5))

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    totalLength = 0
    listOfValues = aDict.values()
    i = 0
    
    
    while (i <= (len(aDict)-1)):
        totalLength =  totalLength + len(listOfValues[i])
        i = i+ 1
    
    return totalLength
    
    
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    listOfValues = aDict.values()
    listOfKeys = aDict.keys()
    i = 0
    value = len(listOfValues)
    value2 = 0

    
    while (i <= (len(aDict)-1)):
        if(value2 < len(listOfValues[i])):
            value2 = len(listOfValues[i])
            value = listOfKeys[i]
        i = i + 1
    
    return value
    