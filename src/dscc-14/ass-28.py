def convert_content(filename, choice):
    try:
        # Open file in read mode
        file = open(filename, "r")

        content = file.read()

        file.close()

        # Switch case operation
        match choice:

            case 1:
                # Convert lowercase to uppercase
                converted_content = content.upper()
                print("Uppercase Content:")
                print(converted_content)

            case 2:
                # Convert uppercase to lowercase
                converted_content = content.lower()
                print("Lowercase Content:")
                print(converted_content)

            case _:
                print("Invalid choice.")

    except FileNotFoundError:
        print("Error: File does not exist.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as error:
        print("Error:", error)


def main():
    # Input file name
    filename = input("Enter file name: ")

    # Display menu
    print("1. Convert to Uppercase")
    print("2. Convert to Lowercase")

    # Input choice
    choice = int(input("Enter your choice: "))

    # Convert file content
    convert_content(filename, choice)


if __name__ == "__main__":
    main()
