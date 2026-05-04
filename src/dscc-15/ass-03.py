import string


def count_words(filename):
    word_count = {}

    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()

        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

        words = text.split()

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count


def main():
    filename = "ass-03-res.txt"

    result = count_words(filename)

    # Display first 10 word counts as sample
    print("Sample word counts:")
    count = 0
    for word, freq in result.items():
        print(word, ":", freq)
        count += 1
        if count == 10:
            break


if __name__ == "__main__":
    main()
