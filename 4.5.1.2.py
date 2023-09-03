s = input("Enter 1 for imperial or 2 for metric")

def bmi(weight, height, s):
    if s == "2":
        if height < 1.0 or height > 2.5 or \
        weight < 20 or weight > 200:
            print("Your inputs of height: ", height, " and weight: ", weight, " were invalid.")
            return None
        else:
            return weight / height ** 2
    elif s == '1':
        if height < .25 or height > 10 or \
        weight < 5 or weight > 450:
            print("Your inputs of height: ", height, " and weight: ", weight, " were invalid.")
            return None
        else:
            return weight / height ** 2
    
    else:
        print("You have not entered a valid system of Measurement, please try again.")
        selected_system
    

#expected output for 1 = success, 2 = error message
print(bmi(352.5, 1.65, s))

