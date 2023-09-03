def check_values(weight,height):
    if 0 < weight < 200:
        if 0 < height < 3:
            return True
        else:
            return False
    else:
        return False

def bmi(weight, height):
    if check_values(weight, height):
        return weight / height ** 2
    else:
        print("Your values are not within a reasonable range, please check your input.")
        return None


print(bmi(52.5, 1.65))
print(bmi(-20, 1.65))
print(bmi(52.5, 4))
