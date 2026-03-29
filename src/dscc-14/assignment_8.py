def binarySearch(array: list[int], target: int) -> int:
    lo = 0
    hi = len(array) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1

    return -1


def main() -> None:
    userInput = input("Input an array of integers (sep. by space): ")
    numbers = []

    for num in userInput.split():
        try:
            numbers.append(int(num))
        except ValueError:
            # This will ensure only valid numbers are inserted.
            pass

    target = int(input("Element to search: "))
    idx = binarySearch(numbers, target)

    if idx == -1:
        print("The element wasn't found in the array.")
    else:
        print(f"Index {idx} contains the element.")


if __name__ == "__main__":
    main()
