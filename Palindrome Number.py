number = int(input("Enter a number for the Paildrome Checking Test:"))

temporary = number
reverse = 0

while temporary > 0:
    digit = temporary % 10
    reverse = reverse * 10 + digit
    temporary //= 10

if reverse == number:
    print(f"\n{number} is a palindrome number.")
else:
    print(f"\n{number} is not a palindrome number.")