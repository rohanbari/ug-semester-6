class PascalTriangle:

    # Display Pascal's triangle
    def display_triangle(self, rows):
        for i in range(rows):
            number = 1

            for j in range(rows - i - 1):
                print(" ", end="")

            for j in range(i + 1):
                print(number, end=" ")

                # Calculate next value
                number = number * (i - j) // (j + 1)

            print()


def main():
    # Input number of rows
    rows = int(input("Enter number of rows: "))

    # Create object
    triangle = PascalTriangle()

    # Display triangle
    triangle.display_triangle(rows)


if __name__ == "__main__":
    main()
