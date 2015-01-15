#bubble sort function
#not working.

    




    
people = ["dave", "adam",  "jesus", "ryan"]
print(people)

sort = False
counter = 0 

while not sort and counter < len(people):
    
    position1 = people[0]
    position2 = people[1]

    if  position1 > position2:
        
        temp = position2
        position2 = position1
        position1 = temp


print(people)

