def process_file(filename):
    try:
        # Open and read file
        file = open(filename, "r")
        content = file.read()
        file.close()

        # Check if 'I' exists
        if 'I' in content:
            print("'I' exists in the file.")

            # Remove all occurrences of 'I'
            updated_content = content.replace('I', '')

            print("Updated content:")
            print(updated_content)

        else:
            print("'I' is absent in the file.")

            # Input another character
            char = input("Enter another character: ")

            print("Entered character:", char)

    except FileNotFoundError:
        print("File not found.")


def main():
    # Input file name
    filename = input("Enter file name: ")

    # Process file
    process_file(filename)


if __name__ == "__main__":
    main()
