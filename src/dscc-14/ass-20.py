def find_longest_lines(filename):
    # read all lines
    with open(filename, 'r') as file:
        lines = file.readlines()

    # remove newline characters
    lines = [line.strip() for line in lines]

    # initial maximum length
    max_len = len(lines[0]) if lines else 0

    # find maximum length
    for line in lines:
        if len(line) > max_len:
            max_len = len(line)

    # collect lines with maximum length
    longest_lines = []
    for line in lines:
        if len(line) == max_len:
            longest_lines.append(line)

    return max_len, longest_lines


def main():
    filename = input("Enter file name: ")
    max_len, lines = find_longest_lines(filename)

    print("Longest line length:", max_len)
    print("Line(s) with maximum length:")
    for line in lines:
        print(line)


if __name__ == '__main__':
    main()
