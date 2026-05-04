import math
import random


def generate_data(n=1000):
    data = []
    for _ in range(n):
        data.append(random.randint(1, 100))  # random numbers between 1 and 100
    return data


def compute_mean(data):
    return sum(data) / len(data)


def compute_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2


def compute_std(data, mean):
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)


def main():
    data = generate_data()

    print("First 50 generated data (not exhaustive):")
    print(data[:50])

    mean = compute_mean(data)
    median = compute_median(data)
    std_dev = compute_std(data, mean)

    print("Mean:", mean)
    print("Median:", median)
    print("Standard Deviation:", std_dev)


if __name__ == "__main__":
    main()
