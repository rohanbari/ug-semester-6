import numpy as np


def main():
    # Define vectors
    u = np.array([1, 2, 3])
    v = np.array([4, -1, 2])

    while True:
        # Display menu
        print("\nMenu")
        print("1. Vector Addition")
        print("2. Scalar Multiplication")
        print("3. Dot Product")
        print("4. Orthogonality Check")
        print("5. Verify Cauchy-Schwarz Inequality")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                # Vector addition
                result = np.add(u, v)
                print("u + v =", result)

            case 2:
                # Scalar multiplication
                result = 2 * u
                print("2u =", result)

            case 3:
                # Dot product
                result = np.dot(u, v)
                print("Dot Product =", result)

            case 4:
                # Orthogonality check
                if np.dot(u, v) == 0:
                    print("Vectors are orthogonal.")
                else:
                    print("Vectors are not orthogonal.")

            case 5:
                # Verify Cauchy-Schwarz inequality
                dot_product = abs(np.dot(u, v))

                norm_u = np.linalg.norm(u)
                norm_v = np.linalg.norm(v)

                print("|u·v| =", dot_product)
                print("||u|| × ||v|| =", norm_u * norm_v)

                if dot_product <= (norm_u * norm_v):
                    print("Cauchy-Schwarz inequality is verified.")
                else:
                    print("Cauchy-Schwarz inequality is not verified.")

            case 6:
                print("Program terminated.")
                break

            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
