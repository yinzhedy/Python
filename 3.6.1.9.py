my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
done = False
passes = 0

while not done:
    #for every number in my_list
    for number in my_list:
        #see if that number exists in my_list
        if number in my_list:
            #if it does then
            #delete my_list at that index
            del my_list[number]
            #Increment passes by one
            passes += 1
            #if number is not in my_list
        elif number not in my_list:
            #move onto the next pass
            continue
    #when all passes are done, stop the while loop
    done = True
            
    
    
#
print("The list with unique elements only:")
print(my_list)
