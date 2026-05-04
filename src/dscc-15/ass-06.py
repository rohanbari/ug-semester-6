import numpy as np
import pandas as pd


def fillmissing_with_mean(df):
    for col in df.select_dtypes(include=['number']).columns:
        df.fillna({col: df[col].mean()}, inplace=True)
    return df


def main():
    # Step 2: Read dataset
    url = "https://media.githubusercontent.com/media/neurospin/pystatsml/refs/heads/master/datasets/iris.csv"
    df = pd.read_csv(url)

    # Step 3: Print column names
    print("Columns:", df.columns.tolist())

    # Step 4: Get numerical columns
    num_cols = df.select_dtypes(include=['number']).columns
    print("Numerical Columns:", list(num_cols))

    # Step 5: Mean by species
    grouped_mean = df.groupby('species')[num_cols].mean()
    print("\nMean values by species:\n", grouped_mean)

    # Step 7: Introduce missing values
    df.iloc[0, 0] = np.nan
    df.iloc[5, 2] = np.nan

    print("\nData with missing values:\n", df.head())

    # Step 8 & 9: Fill missing values
    df = fillmissing_with_mean(df)

    print("\nData after filling missing values:\n", df.head())


if __name__ == "__main__":
    main()
