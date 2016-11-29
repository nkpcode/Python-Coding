def recurPower(base, exp):
    ''',
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if(exp == 1):
        return base
    elif(exp == 0):
        return 1
    else:
        return base*recurPower(base, (exp-1))

#print str(recurPower(1.3,0))

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp == 0:
        return 1
    elif (exp%2) == 0:
        return recurPowerNew(base*base, exp/2)
    elif (exp%2) != 0:
        return base*recurPowerNew(base, exp-1)
        
#print recurPowerNew(2, 4)

def gcdIter(a, b):
    '''
    a, b: positive integers
    9,12
    returns: a positive integer, the greatest common divisor of a & b.
    
    '''
    maximum = max(a,b)
    minimum = min(a,b)
    keep_min = min(a,b)
    result = 0
    
    while(minimum >= 1):
        if(maximum % minimum == 0) and (keep_min % minimum == 0):
            result = minimum
            break
        else:
            minimum = minimum -1
                     
    return result
    
#print gcdIter(9,12)

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcdRecur(b,a%b)

#print gcdRecur(9,12)

def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    count = 0
    for c in aStr:
        count = count + 1
    
    return count    
    
#print str(lenIter("abba"))
    
def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    if(aStr == ""):
        return 0
    else:
        return (1 + lenRecur(aStr[0:-1]))
    
#print lenRecur("ababa")

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    length = len(aStr)
    length_half = length/2
    
    if (length > 1):
        if(char == aStr[length_half]):
            return True
        
        elif(char < aStr[length_half]):
            return isIn(char, aStr[0:length_half])
        
        elif(char > aStr[length_half]):
            return isIn(char, aStr[length_half:])
        
    else:
        if(char == aStr):
            return True
        else:
            return False
            

#print isIn("a","abc")


#wrapper function for recursive function
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
    
def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    length_str1 = len(str1)
    length_str2 = len(str2)
    
    if(length_str1 != length_str2):
        return False
    
    #for the last character
    elif (length_str1 == 1):
        if(str1 == str2):
            return True
        else:
            return False
            
    # for other lenghts    
    elif(str1[0] == str2[length_str2-1]):
        return semordnilap(str1[1:], str2[:(length_str2-1)])
    else:
        return False

print str(semordnilapWrapper("god", "dog"))