user_input = str(input("Please Enter a Word:"))

while user_input != "chupacabra":
    user_input = str(input("Please try again!:"))
    if user_input == "chupacabra":
        print("You've successfully left the loop.")
        break