#import math library to use the value of pi and to compute the tanget
import math

def polysum(n,s):
    """
    Function accepts number of sides of a regular polygon "n"
    and length of each side "s"
    
    Returns (area + perimeter*perimeter)
    """
    
    area = (0.25*n*s*s) * 1.0/(math.tan (math.pi/n))
    
    perimeter = n*s
    
    result = area + (perimeter**2)
    result = round(result,4)
    
    return result
    
#for testing the funcion
#print polysum(3,3)
    
    