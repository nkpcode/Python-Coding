#s = "azcbobobegghakl"
#change the one line code comment
length = len(s)
#print str(length)
#print s[0]
#print s[1]

counter = 0
vowel_count = 0

while (counter < length):
    if (s[counter] == "a" or s[counter] == "e" or s[counter] == "i" \
        or s[counter] == "o" or s[counter] == "u"):
        vowel_count = vowel_count + 1
        
    counter = counter + 1      
print "Number of vowels: "+str(vowel_count)        
    