#test_string = "salad water hamburger salad hamburger" 


def item_order(input_order):
    """
    check what the order is and return consolidated string
    """
    len_order = len(input_order)
    counter = 0
    salad_count = 0
    hb_count = 0
    water_count = 0
    len_salad = len("salad")
    len_hb = len("hamburger")
    len_water = len("water")
    
            
    while(counter < len_order):
        if(((len_order - 1) - counter >= (len_salad - 1)) or 
            ((len_order - 1) - counter >= (len_hb - 1)) or 
            ((len_order - 1) - counter  >= (len_water - 1))):
        #check if the number of characters left are greater than/equal to the
        #remaining characters in the input string    
            
            if (input_order[counter:(counter + len_salad)] == "salad"):
                salad_count = salad_count + 1
                counter = counter + len_salad #if this has been checked 
                #displace the pointer by the length of the character
        
            
            elif (input_order[counter:(counter + len_hb)] == "hamburger"):
                hb_count = hb_count + 1
                counter = counter + len_hb
            
        
            elif (input_order[counter:(counter + len_water)] == "water"):
                water_count = water_count + 1
                counter = counter + len_water
           
            else:
                counter = counter + 1

                        
        else:
            counter = counter + 1
        
        
    #print "salad:"+str(salad_count)+" hamburger:"+str(hb_count)+" water:"+str(water_count)
                
    return "salad:"+str(salad_count)+" hamburger:"+str(hb_count)+" water:"+str(water_count)
    
#item_order(test_string)
