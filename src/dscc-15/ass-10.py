def vector_addition(u, v):
    return [u[i] + v[i] for i in range(3)]


def scalar_multiplication(vector, scalar):
    return [scalar * value for value in vector]


def dot_product(u, v):
    return sum(u[i] * v[i] for i in range(3))


def cross_product(u, v):
    return [
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0]
    ]


def check_orthogonal(u, v):
    return dot_product(u, v) == 0


def check_parallel(u, v):
    cross = cross_product(u, v)
    return cross == [0, 0, 0]


def main():
    # Input vectors
    u = list(map(int, input("Enter vector u (3 values): ").split()))
    v = list(map(int, input("Enter vector v (3 values): ").split()))

    while True:
        # Display menu
        print("\nMenu")
        print("1. Vector Addition")
        print("2. Scalar Multiplication")
        print("3. Dot Product")
        print("4. Cross Product")
        print("5. Orthogonality Check")
        print("6. Parallelism Check")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                result = vector_addition(u, v)
                print("Vector Addition:", result)

            case 2:
                scalar = int(input("Enter scalar value: "))
                result = scalar_multiplication(u, scalar)
                print("Scalar Multiplication:", result)

            case 3:
                result = dot_product(u, v)
                print("Dot Product:", result)

            case 4:
                result = cross_product(u, v)
                print("Cross Product:", result)

            case 5:
                if check_orthogonal(u, v):
                    print("Vectors are orthogonal.")
                else:
                    print("Vectors are not orthogonal.")

            case 6:
                if check_parallel(u, v):
                    print("Vectors are parallel.")
                else:
                    print("Vectors are not parallel.")

            case 7:
                print("Program terminated.")
                break

            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
