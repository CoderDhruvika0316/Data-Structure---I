def SoE(number):
    prime = [True for i in range(number + 1)]
    small = 2

    while (small * small <= number):
        if (prime[small] == True):
            for i in range(small * small, number + 1, small):
                prime[i] = False

        small += 1

    for small in range(2, number + 1):
        if prime[small]:
            print(small)

limit = int(input("Enter a number:"))
print(f"The following are the prime numbers smaller than or equal to {limit}:")
SoE(limit)