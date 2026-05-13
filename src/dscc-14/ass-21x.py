def process_file(filename):
    # read file content
    with open(filename, 'r') as file:
        content = file.read()

    words = content.split()

    # check for standalone 'I'
    if 'I' not in words:
        new_char = input("Enter another character: ")
        content += new_char
        words = content.split()

    # remove standalone 'I'
    updated_words = []
    for word in words:
        if word != 'I':
            updated_words.append(word)

    # join words back
    updated_content = ' '.join(updated_words)

    return updated_content


def main():
    filename = input("Enter file name: ")
    result = process_file(filename)
    print("Updated content:")
    print(result)


if __name__ == '__main__':
    main()
