import numpy as np


def input_matrix(n):
    matrix = []

    # Input matrix elements
    for i in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)

    return np.array(matrix)


def main():
    # Input matrix order
    n = int(input("Enter order of square matrix: "))

    print("Enter matrix elements:")
    A = input_matrix(n)

    while True:
        # Display menu
        print("\nMenu")
        print("1. Determinant")
        print("2. Inverse")
        print("3. Transpose")
        print("4. Scalar Multiplication")
        print("5. Adjoint")
        print("6. Rank")
        print("7. Diagonal Elements")
        print("8. Trace")
        print("9. Eigen Values and Eigen Vectors")
        print("10. Exit")

        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                # Determinant
                print("Determinant:")
                print(np.linalg.det(A))

            case 2:
                # Inverse
                try:
                    print("Inverse:")
                    print(np.linalg.inv(A))
                except np.linalg.LinAlgError:
                    print("Matrix is singular. Inverse does not exist.")

            case 3:
                # Transpose
                print("Transpose:")
                print(A.T)

            case 4:
                # Scalar multiplication
                scalar = float(input("Enter scalar value: "))

                print("Result:")
                print(scalar * A)

            case 5:
                # Adjoint
                try:
                    determinant = np.linalg.det(A)
                    inverse = np.linalg.inv(A)

                    adjoint = determinant * inverse

                    print("Adjoint:")
                    print(adjoint)

                except np.linalg.LinAlgError:
                    print("Adjoint cannot be computed.")

            case 6:
                # Rank
                print("Rank:")
                print(np.linalg.matrix_rank(A))

            case 7:
                # Diagonal elements
                print("Diagonal Elements:")
                print(np.diag(A))

            case 8:
                # Trace
                print("Trace:")
                print(np.trace(A))

            case 9:
                # Eigen values and vectors
                values, vectors = np.linalg.eig(A)

                print("Eigen Values:")
                print(values)

                print("Eigen Vectors:")
                print(vectors)

            case 10:
                print("Program terminated.")
                break

            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
