import math


def isKmurthy(num) -> bool:
    sumFactDigits = 0
    temp = num
    while temp > 0:
        sumFactDigits += math.factorial(temp % 10)
        temp //= 10

    return num == sumFactDigits


lower = int(input("Lower range: "))
upper = int(input("Upper range: "))

for i in range(lower, upper + 1):
    if isKmurthy(i):
        print(i)
