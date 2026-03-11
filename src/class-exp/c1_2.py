# Conditions in Python

def isEvenOdd(num) -> None:
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")


def isEvenOdd2(num) -> None:
    isEven = num % 2 == 0
    print("The number", num, "is", "even." if isEven else "odd.")


def main():
    # Python program to check if a number is even or odd
    num = int(input("Input a number: "))

    isEvenOdd(num)
    isEvenOdd2(num)


if __name__ == "__main__":
    main()
