def reverse_words(text):
    # Split the string into words
    words = text.split()

    # Reverse the list of words
    reversed_words = words[::-1]

    # Join the reversed words
    result = " ".join(reversed_words)

    return result


def main():
    # Input string
    text = input("Enter a string: ")

    # Reverse word order
    reversed_text = reverse_words(text)

    # Display result
    print("Reversed string:", reversed_text)


if __name__ == "__main__":
    main()
