import sys


def find_words(words):
    # Find smallest and longest words
    smallest_word = min(words, key=len)
    longest_word = max(words, key=len)

    return smallest_word, longest_word


def main():
    # Get command line arguments
    words = sys.argv[1:]

    # Check if words are provided
    if len(words) == 0:
        print("Please provide words as command line arguments.")
        return

    # Find required words
    smallest_word, longest_word = find_words(words)

    # Display results
    print("Smallest word:", smallest_word)
    print("Length:", len(smallest_word))

    print("Longest word:", longest_word)
    print("Length:", len(longest_word))


if __name__ == "__main__":
    main()
