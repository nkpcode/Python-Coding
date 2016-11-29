def Primes():
    number = 2
    list_primes = []
    prime = True
    
    while 1:
        
        
        if (prime == True):         
            yield number
            list_primes.append(number)
        else:
            prime = True
        
        number = number + 1
        
        for i in list_primes:
            if (float(number % i) == 0):
                prime = False
                #print prime
        
            