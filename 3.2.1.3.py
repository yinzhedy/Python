secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

input_number = (int(input("Guess a number! (whole numbers only please.)")))
while input_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    input_number = int(input("Pick another whole number!"))
print("Well done, muggle! You are free now.")
