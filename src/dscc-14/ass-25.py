def find_largest_lines(filename):
    try:
        # Open file
        file = open(filename, "r")

        lines = file.readlines()

        file.close()

        # Check empty file
        if len(lines) == 0:
            print("File is empty.")
            return

        max_length = 0
        largest_lines = []

        # Find maximum line length
        for line in lines:
            length = len(line.strip())

            if length > max_length:
                max_length = length
                largest_lines = [line.strip()]

            elif length == max_length:
                largest_lines.append(line.strip())

        # Display result
        print("Line(s) with largest length:")

        for line in largest_lines:
            print(line)

        print("Largest Length:", max_length)

    except FileNotFoundError:
        print("Error: File does not exist.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as error:
        print("Error:", error)


def main():
    # Input file name
    filename = input("Enter file name: ")

    # Find largest lines
    find_largest_lines(filename)


if __name__ == "__main__":
    main()
