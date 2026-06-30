import numpy as np


def main():
    # Input number of vectors
    n = int(input("Enter the number of vectors: "))

    vectors = []
    scalars = []

    # Input vectors and scalars
    for i in range(n):
        vector = list(map(float, input(
            f"Enter 3 elements of vector u{i + 1}: ").split()))
        scalar = float(input(f"Enter scalar a{i + 1}: "))

        vectors.append(np.array(vector))
        scalars.append(scalar)

    # Initialize result vector
    result = np.zeros(3)

    # Compute linear combination
    for i in range(n):
        result += scalars[i] * vectors[i]

    # Display result
    print("\nLinear Combination:")
    print(result)

    # Check zero vector
    if np.allclose(result, np.zeros(3)):
        print("The resulting vector is the zero vector.")
        print("The given vectors may be linearly dependent.")
    else:
        print("The resulting vector is not the zero vector.")
        print("The given vectors are not linearly dependent based on this result.")


if __name__ == "__main__":
    main()
