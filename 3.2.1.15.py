input_number = int(input("Please enter an integer:"))
steps = 0

while input_number != 1:
    if (input_number % 2) == 0:
        input_number = input_number // 2
        steps += 1
        print(input_number)
        continue
    else:
        input_number = input_number * 3 + 1
        steps += 1
        print(int(input_number))
        continue
        
print("steps=", int(steps))