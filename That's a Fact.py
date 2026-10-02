number = int(input("Enter the number which you want to find the factors of:"))

def factors(num):
    print(f"\nThe factors of the number {num} are:")

    for fact in range(1, num + 1):
        if num % fact == 0:
            print(fact)

factors(number)