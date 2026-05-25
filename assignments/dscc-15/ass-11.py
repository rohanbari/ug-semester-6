import numpy as np


def main():
    # Input matrices
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter elements of Matrix A:")
    A = []

    for i in range(rows):
        row = list(map(int, input().split()))
        A.append(row)

    print("Enter elements of Matrix B:")
    B = []

    for i in range(rows):
        row = list(map(int, input().split()))
        B.append(row)

    # Convert lists to numpy arrays
    A = np.array(A)
    B = np.array(B)

    while True:
        # Display menu
        print("\nMenu")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                # Matrix addition
                result = np.add(A, B)

                print("Addition Result:")
                print(result)

            case 2:
                # Matrix subtraction
                result = np.subtract(A, B)

                print("Subtraction Result:")
                print(result)

            case 3:
                # Matrix multiplication
                result = np.matmul(A, B)

                print("Multiplication Result:")
                print(result)

            case 4:
                try:
                    # Matrix division using inverse
                    inverse_B = np.linalg.inv(B)

                    result = np.matmul(A, inverse_B)

                    print("Division Result:")
                    print(result)

                except np.linalg.LinAlgError:
                    print("Matrix B is singular and cannot be inverted.")

            case 5:
                print("Program terminated.")
                break

            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
