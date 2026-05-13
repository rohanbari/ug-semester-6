def main():
    try:
        # Input numbers
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))

        # Division operation
        result = a / b

        print("Result =", result)

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


if __name__ == "__main__":
    main()
