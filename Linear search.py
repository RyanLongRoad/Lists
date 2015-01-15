#Linear list searching

def search_list (to_search, search):
    found = False
    counter = 0

    while not found and counter < len(to_search):
        
        if to_search[counter] == search:
            found = True
            
        else:
            counter = counter + 1

    return found
    

#main program

to_search = ["jesus", "dave", "ryan"]
search = "dave"

found = search_list(to_search, search)

if found:
    print("{0} has been found in the list".format(search))

else:
    print("{0} has not been found in the list".format(search))
