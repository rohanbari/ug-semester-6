import re


def process_string(text, new_number):
    # Extract date
    date = re.search(r"\d{2}/\d{2}/\d{4}", text)

    # Extract time
    time = re.search(r"\d{2}:\d{2}:\d{2}", text)

    # Replace phone number
    updated_text = re.sub(r"\+91-\d{10}", "+91-" + new_number, text)

    # Display results
    if date:
        print("Date:", date.group())

    if time:
        print("Time:", time.group())

    print("Updated String:")
    print(updated_text)


def main():
    # Input string
    text = input("Enter the string: ")

    # Input new phone number
    new_number = input("Enter new 10-digit phone number: ")

    # Process string
    process_string(text, new_number)


if __name__ == "__main__":
    main()
