def is_prime(num):
    prime = True
#
# Write your code here.
    if num > 0:
        for i in range(2, int(num**0.5)+ 1):
            if num % i == 0:
                prime = False
            else:
                continue

    else:
        prime = False
    
    return prime
#

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
