number = int(input("Enter a number (try 5, 10, or 50):"))

input("One loop - runs once per item. Press Enter to run:")

for loop in range(number):
    pass
print(f"\nNumber : {number} | Steps : {number}   ->   O(1) - Linear Time")

input("\nDouble loop - runs 'number x number' per item. Press Enter to run:")

for outer in range(number):
    for inner in range(number):
        pass

print(f"\nNumber : {number} | Steps : {number * number}   ->   O(number ^ 2) - Quadratic Time")

input("\nRule : Count the Loops. Press Enter to run:")

print("\n->0 loops - O(1)\n->1 loop - O(number)\n->2 loops (nested) - O(number ^ 2)")