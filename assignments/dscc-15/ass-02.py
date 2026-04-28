def remove_adj_dups(elements):
    if not elements:
        return []

    result = [elements[0]]

    # Removal of adjacent elements
    # Note: It does not removes ALL duplicates but closest ones!
    for i in range(1, len(elements)):
        if elements[i] != elements[i - 1]:
            result.append(elements[i])

    return result


def main():
    # Test cases
    print("Test Case 1:", remove_adj_dups([1, 2, 2, 3, 2]))  # [1, 2, 3, 2]
    print("Test Case 2:", remove_adj_dups([4, 4, 4, 4]))     # [4]
    print("Test Case 3:", remove_adj_dups([1, 2, 3, 4]))     # [1, 2, 3, 4]


if __name__ == "__main__":
    main()
