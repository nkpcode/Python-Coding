x = 12345
epsilon = 0.0000000001 #tolerence allowed between calculated value and required value 
low = 0.0
high = x
ans = (low + high)/2.0
numberOfGuesses = 0

while abs(ans**2 - x) >= epsilon:
    if(ans**2 > x):
        high = ans
    elif(ans**2 < x):
        low = ans
    numberOfGuesses = numberOfGuesses + 1
    ans = (low + high)/2.0
    
print ("The closest possible value calculated is "+str(ans))