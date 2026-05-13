import statistics


def calculate_statistics(numbers):
    # Calculate statistical values
    mean_value = statistics.mean(numbers)
    median_value = statistics.median(numbers)
    mode_value = statistics.mode(numbers)
    variance_value = statistics.variance(numbers)
    std = statistics.stdev(numbers)

    return mean_value, median_value, mode_value, variance_value, std


def main():
    # Input list elements
    numbers = list(map(float, input(
        "Enter numbers separated by space: ").split()))

    # Calculate statistics
    mean_value, median_value, mode_value, variance_value, std = (
        calculate_statistics(numbers)
    )

    # Display results
    print("Mean:", mean_value)
    print("Median:", median_value)
    print("Mode:", mode_value)
    print("Variance:", variance_value)
    print("Standard Deviation:", std)


if __name__ == "__main__":
    main()
