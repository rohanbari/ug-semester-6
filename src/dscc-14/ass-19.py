def main():
    try:
        # Input integer
        number = int(input("Enter an integer: "))

        print("You entered:", number)

    except ValueError:
        print("Error: Invalid integer input.")


if __name__ == "__main__":
    main()
