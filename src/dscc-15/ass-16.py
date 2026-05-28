import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def main():
    # Load Iris dataset
    iris = load_iris()

    X = iris.data
    y = iris.target
    target_names = iris.target_names

    # Standardize features
    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    # Apply PCA
    pca = PCA(n_components=2)

    principal_components = pca.fit_transform(X_scaled)

    # Create DataFrame
    pca_df = pd.DataFrame(
        data=principal_components,
        columns=["PC1", "PC2"]
    )

    pca_df["Species"] = y

    # Plot PCA result
    plt.figure(figsize=(8, 6))

    for species in range(len(target_names)):
        plt.scatter(
            pca_df[pca_df["Species"] == species]["PC1"],
            pca_df[pca_df["Species"] == species]["PC2"],
            label=target_names[species]
        )

    # Graph labels
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")

    plt.title("PCA on Iris Dataset")

    plt.legend()

    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    main()
