def bubbleSort(array: list[int]) -> None:
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def main() -> None:
    userInput = input("Input an array of integers (sep. by space): ")
    numbers = []

    for num in userInput.split():
        try:
            numbers.append(int(num))
        except ValueError:
            # This will ensure only valid numbers are inserted.
            pass

    print("Before sort:", numbers)
    bubbleSort(numbers)
    print("After  sort:", numbers)


if __name__ == "__main__":
    main()
