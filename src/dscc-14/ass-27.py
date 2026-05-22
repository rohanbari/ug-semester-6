import sys


def copy_file(source_file, destination_file):
    try:
        # Open source file
        source = open(source_file, "r")

        # Read content
        content = source.read()

        source.close()

        # Open destination file
        destination = open(destination_file, "w")

        # Write content
        destination.write(content)

        destination.close()

        print("File copied successfully.")

    except FileNotFoundError:
        print("Error: Source file does not exist.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as error:
        print("Error:", error)


def main():
    # Check command line arguments
    if len(sys.argv) != 3:
        print("Usage: python program.py <source_file> <destination_file>")
        return

    source_file = sys.argv[1]
    destination_file = sys.argv[2]

    # Check same file names
    if source_file == destination_file:
        print("Error: Source and destination files must be different.")
        return

    # Copy file content
    copy_file(source_file, destination_file)


if __name__ == "__main__":
    main()
