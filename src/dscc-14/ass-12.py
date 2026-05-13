def find_numbers(start, end):
    result = []

    # Check numbers in the given range
    for num in range(start, end + 1):
        if num % 7 == 0 and num % 10 == 6:
            result.append(num)

    return result


def main():
    # Input range
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    # Find required numbers
    numbers = find_numbers(start, end)

    # Display result
    print("Numbers divisible by 7 and ending with 6:")

    for num in numbers:
        print(num, end=" ")


if __name__ == "__main__":
    main()
