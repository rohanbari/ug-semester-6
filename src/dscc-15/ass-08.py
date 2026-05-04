import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def detect_outliers_iqr(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return lower, upper


def main():
    # Step 1: Read dataset
    df = pd.read_csv("ass-08-res.csv")

    print("First 5 rows:\n", df.head())
    print("\nInfo:\n")
    print(df.info())

    # Select numerical columns
    num_cols = df.select_dtypes(include=np.number).columns
    col = "Fare"

    print(f"\nUsing column: {col}")

    # ---------------- UN-CLEANED DATA ----------------
    plt.figure()
    plt.hist(df[col], bins=20)
    plt.title("Histogram (Uncleaned Data)")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()

    plt.figure()
    sns.boxplot(x=df[col])
    plt.title("Boxplot (Uncleaned Data)")
    plt.show()

    # ---------------- CLEANING ----------------
    # Handle missing values
    df[col] = df[col].fillna(df[col].median())

    # Detect outliers
    lower, upper = detect_outliers_iqr(df[col])

    # Mark outliers
    outliers = df[(df[col] < lower) | (df[col] > upper)]

    print("\nOutliers detected:\n", outliers)

    # Remove outliers
    df_clean = df[(df[col] >= lower) & (df[col] <= upper)]

    # ---------------- CLEANED DATA ----------------
    plt.figure()
    plt.hist(df_clean[col], bins=20)
    plt.title("Histogram (Cleaned Data)")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()

    plt.figure()
    sns.boxplot(x=df_clean[col])
    plt.title("Boxplot (Cleaned Data)")
    plt.show()

    # ---------------- OUTLIER VISUALIZATION ----------------
    plt.figure()
    sns.scatterplot(x=range(len(df)), y=df[col])
    plt.axhline(lower)
    plt.axhline(upper)
    plt.title("Outlier Detection (Scatter Plot)")
    plt.xlabel("Index")
    plt.ylabel(col)
    plt.show()


if __name__ == "__main__":
    main()
