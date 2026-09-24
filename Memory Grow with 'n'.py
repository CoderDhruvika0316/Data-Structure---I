number = int(input("Enter a random number:"))

guess = int(input("Prediction : How many items will be in the list if the number is what you have entered?"))

points = list(range(1, number + 1))

print(f"Your Guess : {guess}   |   List : {points}   |   Items : {len(points)}")

input("\nPrediction : What happens to the list as the number grows? Press Enter:")

for i in [number, 100, 1000]:
    print(f"Number = {i :< 5}   |   List uses : {i :> 5} items in memory")