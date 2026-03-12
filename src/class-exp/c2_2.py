import math


def isPrime(num: int) -> bool:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


lower = int(input("Provide the lower range: "))
upper = int(input("Provide the upper range: "))

for i in range(lower, upper + 1):
    if isPrime(i):
        print(i)
