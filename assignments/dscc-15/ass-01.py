def calc(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Invalid operation"


def main():
    # Test cases
    print("Test Case 1:", calc(4, 5, "multiply"))   # Expected: 20
    print("Test Case 2:", calc(3, 5))               # Expected: 8
    print("Test Case 3:", calc(1, 2, "something"))  # Expected: Error


if __name__ == "__main__":
    main()
