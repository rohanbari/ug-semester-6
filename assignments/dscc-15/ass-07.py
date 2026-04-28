import matplotlib.pyplot as plt
import numpy as np


def main():
    # Generate datasets
    male = np.random.normal(170, 8, 100)
    female = np.random.normal(160, 7, 100)

    # Boxplot
    plt.figure()
    plt.boxplot([male, female], label=["Male", "Female"])
    plt.title("Boxplot Comparison")
    plt.ylabel("Height")
    plt.show()

    # Median and variability
    male_median = np.median(male)
    female_median = np.median(female)

    male_std = np.std(male)
    female_std = np.std(female)

    print("Male Median:", male_median)
    print("Female Median:", female_median)
    print("Male Std Dev:", male_std)
    print("Female Std Dev:", female_std)

    # Overlapping histograms
    plt.figure()
    plt.hist(male, bins=15, alpha=0.5, label="Male")
    plt.hist(female, bins=15, alpha=0.5, label="Female")
    plt.title("Distribution Overlap")
    plt.xlabel("Height")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
