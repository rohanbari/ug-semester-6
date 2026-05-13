def sort_words(text):
    # Split words using hyphen
    words = text.split("-")

    # Sort words alphabetically
    words.sort()

    # Join sorted words
    result = "-".join(words)

    return result


def main():
    # Input hyphen-separated words
    text = input("Enter hyphen-separated words: ")

    # Sort words
    sorted_text = sort_words(text)

    # Display result
    print("Sorted sequence:", sorted_text)


if __name__ == "__main__":
    main()
