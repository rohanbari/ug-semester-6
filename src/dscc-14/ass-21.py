def main():
    try:
        # Open file
        file = open("sample.txt", "r")

        content = file.read()

        print(content)

        file.close()

    except FileNotFoundError:
        print("Error: File does not exist.")


if __name__ == "__main__":
    main()
