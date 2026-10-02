number = int(input("Enter a number (try 3 or 5):"))
guess = input("Guess how many times the countdown call itself for the number {number}:")

input("Recursion - Watch each and every call. Press Enter to run:")

def countdown(num):
    print(f"Call - Number {num}")

    if num > 0:
        countdown(num - 1)

countdown(number)

print(f"Calls : {number + 1} | Your Guess : {guess} -> O(number)")

input("Watch the calls grow with the number. Press Enter to run:")

for call in [5, 10, 100]:
    print(f"Number : {number} | Calls : {call + 1} -> O(number)")