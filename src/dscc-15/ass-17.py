import matplotlib.pyplot as plt
import numpy as np


def main():
    # Family sizes
    family_size = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Absolute frequencies
    frequencies = [26, 21, 17, 12, 9, 3, 2, 2, 1]

    # Calculate cumulative frequencies
    cumulative_frequencies = np.cumsum(frequencies)

    # Plot absolute frequency diagram
    plt.figure(figsize=(8, 5))

    plt.bar(family_size, frequencies)

    plt.xlabel("Family Size")
    plt.ylabel("Absolute Frequency")

    plt.title("Absolute Frequency Distribution")

    plt.grid(True)

    plt.show()

    # Plot cumulative frequency diagram
    plt.figure(figsize=(8, 5))

    plt.plot(
        family_size,
        cumulative_frequencies,
        marker="o"
    )

    plt.xlabel("Family Size")
    plt.ylabel("Cumulative Frequency")

    plt.title("Cumulative Frequency Distribution")

    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    main()
