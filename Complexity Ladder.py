guess = input("Guess how many steps it will take to use O(number ^ 2) if the number = 1000:")

input("Watch O(number) and O(number ^ 2) grow. Press Enter to run:")

for num in [10, 100, 1000]:
    input(f"\nNumber : {num}. Press Enter to run:")
    print(f"O(number) : {num}  |  O(number ^ 2) : {num * num}")

print(f"\nYour Guess : {guess}")
input("\nFull Complexity Ladder is at 1000. Press Enter to run:")

print("\n O(1) : 1  |  O(log number) : 10  |  O(number) : 1000  |  O(number ^ 2) : 1000000")