def count_occurrences(arr, element):
    count = 0

    # Count matching elements
    for item in arr:
        if item == element:
            count += 1

    return count


def main():
    # Input array elements
    arr = list(map(int, input("Enter elements separated by space: ").split()))

    # Input element to search
    element = int(input("Enter element to count: "))

    # Count occurrences
    result = count_occurrences(arr, element)

    # Display result
    print("Number of occurrences:", result)


if __name__ == "__main__":
    main()
