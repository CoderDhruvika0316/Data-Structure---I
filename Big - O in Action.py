number = int(input("Enter the number you will be working with:"))
guess = int(input("Guess how many pairs are there:"))

step = 1
print(f"\nCONSTANT TIME (O(1)) ->  Steps : {step}")

step = 0
for i in range(number):
    step += 1

print(f"LINEAR TIME (O(number)) ->  Steps : {step}")

step = 0

for i in range(number):
    for j in range(number):
        step += 1

print(f"QUADRATIC TIME (O(n ^ 2)) ->  Guess : {guess}   |   Steps : {step}")