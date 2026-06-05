import pandas as pd
from scipy.stats import kurtosis, skew
from sklearn.datasets import load_iris


def main():
    # Load Iris dataset
    iris = load_iris()

    # Create DataFrame
    df = pd.DataFrame(
        iris.data,
        columns=iris.feature_names
    )

    # Select sepal length
    sepal_length = df["sepal length (cm)"]

    # Calculate skewness
    skewness = skew(sepal_length)

    # Calculate kurtosis
    kurt = kurtosis(sepal_length)

    # Display results
    print("Skewness:", skewness)

    print("Kurtosis:", kurt)

    # Interpretation
    if skewness > 0:
        print("Distribution is positively skewed.")

    elif skewness < 0:
        print("Distribution is negatively skewed.")

    else:
        print("Distribution is symmetric.")

    if kurt > 0:
        print("Distribution is leptokurtic.")

    elif kurt < 0:
        print("Distribution is platykurtic.")

    else:
        print("Distribution is mesokurtic.")


if __name__ == "__main__":
    main()
