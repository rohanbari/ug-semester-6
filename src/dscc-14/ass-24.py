def print_triplets(limit):
    # Find Pythagorean triplets
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            for c in range(b, limit + 1):
                # Check Pythagorean condition
                if (a ** 2) + (b ** 2) == (c ** 2):
                    print(a, b, c)


def main():
    # Input range limit
    limit = int(input("Enter the range limit: "))

    # Display triplets
    print("Pythagorean Triplets:")

    print_triplets(limit)


if __name__ == "__main__":
    main()
