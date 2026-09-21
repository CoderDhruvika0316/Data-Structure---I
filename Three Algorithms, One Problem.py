#Formula
number = int(input("Enter the number of students who earned scores:"))
guess = input("Guess the total points you think the students have earned:")

total = number * (number + 1)  // 2
print(f"Formula\nTotal : {total}   |   Steps : 1")


#Single Loop
total = 0

for i in range(1, number + 1):
    total += i
print(f"\nSingle Loop\nTotal : {total}   |   Steps : {number}")

#Double Loop
total = 0
steps = 0

for i in range(1, number + 1):
    for j in range(1,  i + 1):
        total += 1
        steps += 1

print(f"\nDouble Loop\nTotal : {total}   |   Steps : {steps}")

print(f"\nYour guess: {guess}   |   Answer : {total}")