# Program to guess the number chosen by the user

high = 100
low = 0
guess_ans = (high + low)/2 #starting the binary search

# Asking the user if answer is right or wrong
print "Please think of a number between 0 and 100!"
option = "x" 

# If not, proceeding with guesses
while (option != "c"):
    
    print "Is your secret number "+str(guess_ans)+"?" 
    option = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    
    # damage control for wrong input entered
    if option != "h" and option != "l" and option != "c":
        print "Sorry, I did not understand your input."
 
    else:
      
        if option == "h" :
    #        print ("Inside h's if")
            high = guess_ans
            guess_ans = (high + low)/2
            
        elif option == "l" :
    #        print ("Inside l's if")
            low = guess_ans
            guess_ans = (high + low)/2    
print "Game over. Your secret number was:",
print str(guess_ans)