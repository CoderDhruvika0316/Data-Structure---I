number = int(input("Enter a number:"))

digits = len(str(number))

result = 0

temporary = number
while temporary > 0:
    digit = temporary % 10
    result += digit ** digits
    temporary //= 10

if number == result:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")