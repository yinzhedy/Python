income = float(input("Enter the annual income: "))

#
# Write your code here.
if income > 85528:
    tax = (14839.02) + 0.32 * (income - 85528)
else:
    tax = (.18 * income) - 556.02
#
if tax < 0:
    tax = 0.
else:
    tax = round(tax, 0.)
print("The tax is:", tax, "thalers")
