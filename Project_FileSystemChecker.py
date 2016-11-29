import json
import time

#!!!!!!!!!!!!!!!!!Assumptions!!!!!!!!!!!!!!!!!
#Only one level of indirection i.e., "indirect" can be 0 or 1


# --------------------------------------
# Change the block numbers accordingly to accomodate all available blocks
begining_block_number = 0 
ending_block_number = 30
BLOCK_SIZE = 4096
MAX_POINTERS_INBLOCK = 400 

global_used_list = []
global_free_list = []

# --------------------------------------
# Performing devID check
def devID_check(value):
    print("Performing Device ID check")
    if (value != 20):
        print("The device ID for this file systesm is 20. Changing the device id to 20")
        block_super["devId"] = 20 
    else:
        print("The device ID passed the check")
    
    print("-------------------------------")
    
    
# --------------------------------------
# Performing Time check
def check_time():
    
    print("Performing time check (time should be in the past) on all relevant blocks")
    now = time.time()
    
    
    
    filename_part = "fusedata."
    i_start = begining_block_number #1
    i_end = ending_block_number #30
    file_name = filename_part

                                                        
    for i in range(i_start, (i_end + 1)):
        #opening each block available to us
        file_name = filename_part + str(i)
        #print "file_name"+file_name
        file_access = open (file_name,"r+")
        
        try:
            block_contents = json.load(file_access)
            file_access.close()
        except ValueError:
            print "\""+file_name+"\" not in json format (catch 1)"
            file_access.close()   
            continue
            
        # first performing the size check
        if(type(block_contents) == dict):
            
            # checking if the current parsed block is a file inode
            if(("creationTime" in block_contents) == True):
                past = block_contents["creationTime"]
                if(past > now):
                    print "creationTime is not a valid in "+file_name
                else:
                    print "creationTime is valid in "+file_name
                    
            if(("atime" in block_contents) == True):
                past = block_contents["atime"]
                if(past > now):
                    print "atime is not valid in "+file_name
                else:
                    print "atime is valid in "+file_name                

            if(("ctime" in block_contents) == True):
                past = block_contents["ctime"]
                if(past > now):
                    print "ctime is not valid in "+file_name
                else:
                    print "ctime is valid in "+file_name                 

            if(("mtime" in block_contents) == True):                        
                past = block_contents["mtime"]
                if(past > now):
                    print "mtime is not valid in "+file_name
                else:
                    print "mtime is valid in "+file_name    
                    

    print("-------------------------------")


# --------------------------------------
# Perform the "." and ".." check
def traverse_block_number_check():
    print("Checking if each block number is mapped correctly in root directory")
    root_block = block_super["root"]
    
    
    # get the contents of root directory
    file_name = "fusedata."+str(root_block)
    file_access = open (file_name,"r+")
    
    block = json.load(file_access)   
    file_access.close()
    
    items = block["filename_to_inode_dict"]

    number_of_items = len(items)
    #print str(number_of_items)
    link_count_check = block["linkcount"]
    
    if(link_count_check != number_of_items):
        print("Link count is incorrect. Changing the value of linkcount")
        block["linkcount"] = number_of_items

    else:
        print("Linkcount check passed.")
            
    #accessing each of the dictionaries 
    for i in range(0 , number_of_items):
        if (items[i]["type"] == "d"):
            #inspect directory
                if(items[i]["name"] == "."):
                    if(items[i]["location"] != root_block):
                        print("Error in \'.\' location information")
                        #+++ change the value of location if wrong
                        items[i]["location"] = root_block
                        print("Error in \'.\' is fixed")
                    else:
                        print("\'.\' test passed")
                
                elif(items[i]["name"] == ".."):
                    if(items[i]["location"] != root_block):
                        print("Error in \'..\' location information")
                        #+++ change the value of location if wrong
                        items[i]["location"] = root_block
                        print("Error in \'..\' is fixed")
                    else:
                        print("\'..\' test passed")    
                
                else:
                    root_directory_path = "root->"+str(items[i]["location"])
                    if(items[i]["location"] != root_block):
                        inspect_dir(items[i],root_directory_path,root_block)
                        global_used_list.append(items[i]["location"])# add to used list
                    else:
                        crap = json.dumps(items[i]) 
                        print "Item with attributes "+crap+" is not valid" 

    #closing the file to effect changes
    #+++ change this
    file_access_3 = open (file_name,"w")
    json.dump(block,file_access_3)
    file_access_3.close()
    print("-------------------------------")
        
# --------------------------------------
# Checking the directory
def inspect_dir(current_directory, root_directory_path, current_directory_parent):
    print "Current Position: "+root_directory_path
    block_current = current_directory["location"]
    

    
    #print current_directory
    file_name = "fusedata."+str(block_current)
    file_access = open (file_name,"r+")
    block_contents = json.load(file_access)  
    file_access.close()
    
    items = block_contents["filename_to_inode_dict"]
    number_of_items = len(items)
    
    #accessing each of the dictionaries 
    for i in range(0 , number_of_items):
        if (items[i]["type"] == "d"):
            #inspect directory
                if(items[i]["name"] == "."):
                    if(items[i]["location"] != block_current):
                        print("Error in \'.\' location information")
                        #+++ change the value of location if wrong
                        items[i]["location"] = block_current
                        print("Error in \'.\' is fixed")
                    else:
                        print("\'.\' test passed")
                
                elif(items[i]["name"] == ".."):
                    if(items[i]["location"] != current_directory_parent):
                        print("Error in \'..\' location information")
                        #+++ change the value of location if wrong
                        items[i]["location"] = block_current
                        print("Error in \'..\' is fixed")
                    else:
                        print("\'..\' test passed")    
                
                else:
                    root_directory_path = root_directory_path+"->"+str(items[i]["location"])
                    if(items[i]["location"] != block_current):
                        inspect_dir(items[i],root_directory_path,block_current)
                        global_used_list.append(items[i]["location"])# add to used list
                    else:
                        crap = json.dumps(items[i]) 
                        print "Item with attributes "+crap+" is not valid" 
    
    #closing the file to effect changes
    file_access_2 = open (file_name,"w")
    json.dump(block_contents,file_access_2)
    file_access_2.close()    

# --------------------------------------
# Checking the directory
def perform_general():

    """
    performs the "indirect" and "size" tests on all the available blocks
    
    """
    print("Performing the \"indirect\" check on all blocks")
        
    filename_part = "fusedata."
    i_start = begining_block_number + 1 #1
    i_end = ending_block_number #25
    file_name = filename_part

                                                        
    for i in range(i_start, (i_end + 1)):
        #opening each block available to us
        file_name = filename_part + str(i)
        #print "file_name"+file_name
        file_access = open (file_name,"r+")
        
        try:
            block_contents = json.load(file_access)
            file_access.close()
        except ValueError:
            print "\""+file_name+"\" not in json format (catch 1)"
            file_access.close()   
            continue
            
        # first performing the size check
        if(type(block_contents) == dict):
            # checking if the current parsed block is a file inode
            if(("indirect" in block_contents) == True):
                size_check(block_contents, file_name)
                perform_indirect(block_contents, file_name)
            
                #closing the file to effect changes
                file_access_2 = open (file_name,"w")
                json.dump(block_contents,file_access_2)
                file_access_2.close()         
    

        
    print("Reached end of test")            
                
    print("-------------------------------")                        
          

    
# --------------------------------------
# Performing indirect check            
def perform_indirect(block_contents, file_name_current):    
    
    indirect_value = block_contents["indirect"]
    location_pointer = block_contents["location"]

    if not(location_pointer in global_used_list):
        global_used_list.append(location_pointer)# add to used list    

    if (indirect_value == 1):
        
        print "Performing the indirect test on "+file_name_current
        file_location_checking = "fusedata." + str(location_pointer)
        #print "file_location_checking = "+ file_location_checking
        file_access = open(file_location_checking, "r")
        
        try:
            block_contents = json.load(file_access)
            if(type(block_contents) == list):
                print "Indirect test passed"
            else:
                print "Error in indirect information. Making corrections."
                block_contents["location"] = 0
                print "Error corrected. \"indirect\" is now 0"             

        except ValueError:
            print "\""+file_access+"\" not in json format (catch 2)"
                
        
        file_access.close()

    elif (indirect_value == 0):
        
        print "Performing the indirect test on "+file_name_current
        file_location_checking = "fusedata." + str(location_pointer)
        #print "file_location_checking = "+ file_location_checking
        file_access = open(file_location_checking, "r")
        
        try:
            block_contents = json.load(file_access)
            if(type(block_contents) == dict):
                print "Indirect test passed"
            elif(type(block_contents) == list):
                print "Error in indirect information. Making corrections."
                block_contents["location"] = 1
                print "Error corrected. \"indirect\" is now 1"             

        except ValueError:
            print "\""+file_access+"\" not in json format (catch 3)"
                
        
        file_access.close()        
        
# --------------------------------------
# Performing indirect check
                

def size_check(block_contents, file_name_current):    
    """
    size<blocksize  should have indirect=0 and size>0
    if indirect!=0, size should be less than (blocksize*length of location array)
    
    """ 
    print "Performing size check on "+file_name_current
    #print block_contents
    size_value = block_contents["size"]
    indirect_value = block_contents["indirect"]
    location_pointer = block_contents["location"]

    if not(location_pointer in global_used_list):
        global_used_list.append(location_pointer)# add to used list   
        
    file_location_checking = "fusedata." + str(location_pointer)
    #print "file_location_checking = "+ file_location_checking

    file_access = open(file_location_checking, "r")
    length_array_location = 1

    try:
        block_contents = json.load(file_access)
        type_contents = type(block_contents)

    except ValueError:
        print "\""+file_access+"\" not in json format (catch 4)"    
        type_contents = None
    
    if(type_contents == list):
        length_array_location = len(block_contents) 
    
    if (size_value < BLOCK_SIZE):
        if(indirect_value == 0):
            if(size_value > 0):
                print("Size test passed")
            else:
                print("Size <= 0")
        else:
            print "Size does not make sense. Not changing the size."            
    
    if(size_value < (BLOCK_SIZE * length_array_location)):
        if(type_contents == list):
            
            if(indirect_value == 1):
                print "Size Test passed (2)"
            else:
                print"Wrong use of indirect. Changing indirect to 1"
                block_contents["indirect"] = 1
                print "Changes made." 
        
        else:
            if(indirect_value != 0):
                print"Wrong use of indirect. Changing indirect to 0"
                block_contents["indirect"] = 0
                print "Changes made."
            
# --------------------------------------
# Performing free block list check
def free_block_list():
    print("Performing free block list check")
    
    i_start = block_super["freeStart"] #1
    i_end = block_super["freeEnd"] #25

    
    for i in range(i_start , (i_end + 1)):
        file_name = "fusedata."+str(i)
        #get contents of block
        file_access = open (file_name,"r")
        
        try:
            current_list = json.load(file_access)
            file_access.close()
            if(type(current_list) != list):
                print("Not in required format: "+ file_name)
                continue
        except ValueError:
            file_access.close()
            continue    
        
        
        current_list.sort()
        current_list_keep = current_list
        length = len(current_list)
        j_start = current_list[0]
        j_end = current_list[length - 1]
        
        
        for j in range(j_start, (j_end + 1)):
            if (not(j in current_list)) and (not(j in global_used_list)):
                #if value not available in current list and not pesent in global list
                #
                print("Appending "+str(j)+" to current list: "+file_name)
                current_list_keep.append(j)
                current_list_keep.sort()
            if (j in global_used_list):
                print("Removing "+str(j)+" from current list: "+file_name+" as it is being used")
                current_list_keep.remove(j)
                
        #put contents of the updated file
        current_list = current_list_keep
        file_access_2 = open (file_name,"w")
        json.dump(current_list, file_access_2)
        file_access_2.close()               
        
    print("Done")             
    print("-------------------------------")
    

          
       
                
                                
                                                                
# +++++++opening the super block+++++++++
parsed_super = open ("fusedata.0","r+")   
block_super = json.load(parsed_super)

#performing devID check
devID_check(block_super["devId"])

#performing time check
check_time()

#perform the "." and ".." check
traverse_block_number_check()

#perform the indirect check on all available blocks
perform_general()

#perform free block list check
free_block_list()





# file "f", directory "d", superblock which is 0th block




