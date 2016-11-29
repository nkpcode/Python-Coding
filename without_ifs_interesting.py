def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
     without using "if" statements
    '''
    #get low
    #(4,7,6)
    #(-1.95, -3.17, 1.51)
    #(-3.3, 4.86, 4.21)
    
    result = min(lo,x)
    while(result == lo):
        result = max(hi,x)
        while(result == hi):
            result = x 
            break
        while(max(hi,x) != hi):
            result = hi
            break
        break
    
    while(min(lo,x) != lo):
       result = lo
       break 
     
    return result
    


print clip(-3.3, 4.86, 4.21)
