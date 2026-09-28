points = [1, 3, 5, 7, 9, 11, 13, 15, 17]

input(f"List : {str(points)} |  Number : 9\nPress Enter to run:")
guess = input("Guess the maximum checks it will take to find any number in this list:")
target = int(input("Pick a number in the list we will start searching for:"))

input("Binary Search : Checks the middle, drops the half each round. Press Enter to run:")

low, high = 0, len(points) - 1
steps = 0

while low <= high:
    mid = (low + high)  // 2
    steps += 1

    print(f"Round {steps}  ->  Checked {points[mid]}")

    if points[mid] == target:
        break
    elif points[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print(f"Found : {target}\nPosition : {mid + 1}\nSteps : {steps}\nYour guess : {guess}\nMethod : [O(log 'n')]")

input("Steps grow slowly with 'n'. pres Enter to run:")

for n, s in [(9, 4), (100, 7), (1000, 10)]:
    print(f"Number : {n}  |  Maximum Steps : {s}  ->  [O(log 'n')]")