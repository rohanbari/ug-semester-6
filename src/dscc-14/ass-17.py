import math


def is_krishnamurthy(number):
    temp = number
    total = 0

    # Calculate sum of factorials of digits
    while temp > 0:
        digit = temp % 10
        total += math.factorial(digit)
        temp //= 10

    return total == number


def main():
    # Input number
    number = int(input("Enter a number: "))

    # Check Krishnamurthy number
    if is_krishnamurthy(number):
        print(number, "is a Krishnamurthy number.")
    else:
        print(number, "is not a Krishnamurthy number.")


if __name__ == "__main__":
    main()
