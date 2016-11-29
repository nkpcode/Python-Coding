s = "aloboobbbobbbobbbobbbboboobbobbbobbbo"
#change the first line code comment
length = len(s)

counter = 0
bob_count = 0

while (counter < (length - 2)):
    if (s[counter] == "b" and s[counter + 1] == "o" and s[counter + 2] == "b"):
        bob_count = bob_count + 1
        
    counter = counter + 1      
print "Number of times bob occurs is: "+str(bob_count)        
    