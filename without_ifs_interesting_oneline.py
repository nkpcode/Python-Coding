def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    #get low
    #(4,7,6)
    #(3,2,5)
    #(-1.95, -3.17, 1.51)
    #(-3.3, 4.86, 4.21)
    
    return min(max(x,lo),hi)
    


print clip(-3.3, 4.86, 4.21)
