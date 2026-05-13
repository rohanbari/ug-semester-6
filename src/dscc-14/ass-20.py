def main():
    try:
        # Create list
        numbers = [10, 20, 30, 40]

        # Input index
        index = int(input("Enter index value: "))

        print("Element =", numbers[index])

    except IndexError:
        print("Error: Index out of range.")


if __name__ == "__main__":
    main()
