blocks = int(input("Enter the number of blocks: "))
layer_number = 1
height = 0
#
# Write your code here.
while blocks >= layer_number:
    height += 1
    blocks -= layer_number
    layer_number += 1

    
#	

print("The height of the pyramid:", height)
