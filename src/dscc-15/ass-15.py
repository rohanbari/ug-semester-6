import numpy as np


def main():
    # Define vectors
    v1 = np.array([1, 1, 0])
    v2 = np.array([0, 1, 1])
    v3 = np.array([1, 2, 1])

    # Form matrix
    A = np.column_stack((v1, v2, v3))

    # Calculate rank
    rank = np.linalg.matrix_rank(A)

    print("Matrix:")
    print(A)

    print("\nRank:", rank)

    # Check linear independence
    if rank == 3:
        print("The vectors are linearly independent.")
    else:
        print("The vectors are linearly dependent.")

    # Find basis
    basis = []

    for i in range(rank):
        basis.append(A[:, i])

    print("\nBasis for the subspace:")

    for vector in basis:
        print(vector)

    # Display dimension
    print("\nDimension of the subspace:", rank)


if __name__ == "__main__":
    main()
