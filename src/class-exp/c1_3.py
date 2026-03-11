# Loops in Python

def sumNums(num: int) -> None:
    currSum = 0
    for i in range(1, num + 1):
        currSum += i

    print("Sum from 1 to", num, "is:", currSum)


def sumNums2(num: int) -> None:
    currSum = sum([n for n in range(1, num + 1)])
    print(f"Sum of first {num} natural numbers is:", currSum)


def sumWhile(num: int) -> None:
    currSum = 0
    while num > 0:
        currSum += num
        num -= 1

    print(f"Sum of first {num} natural numbers:", currSum)


def main() -> None:
    N = int(input("Input the value of N: "))
    sumNums(N)
    sumNums2(N)
    sumWhile(N)


if __name__ == "__main__":
    main()
