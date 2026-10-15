"""Customer Segmentation using K-Means, DBSCAN, and Agglomerative clustering."""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

DATA_FILE = Path(__file__).with_name("customers.csv")


def load_customers():
    """Load customer data and return the table plus scaled feature matrix."""
    data = pd.read_csv(DATA_FILE)
    features = data[["Age", "AnnualIncome", "SpendingScore"]]
    scaler = StandardScaler()  # Scaling prevents income's larger numbers dominating.
    scaled = scaler.fit_transform(features)
    return data, scaled


def kmeans_analysis(data, scaled):
    """Try several K values, print scores, and fit the chosen K-Means model."""
    print("\nK-Means elbow and silhouette check")
    scores = []
    inertias = []
    max_k = min(6, len(data) - 1)
    for k in range(2, max_k + 1):
        model = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = model.fit_predict(scaled)
        inertias.append(model.inertia_)
        scores.append(silhouette_score(scaled, labels))
        print(f"k={k}: inertia={model.inertia_:.3f}, silhouette={scores[-1]:.3f}")
    chosen_k = 3  # Chosen for a simple classroom demonstration; inspect scores too.
    model = KMeans(n_clusters=chosen_k, random_state=42, n_init=10)
    data["KMeansCluster"] = model.fit_predict(scaled)
    print(f"\nK-Means labels assigned using k={chosen_k}.")
    print(data[["CustomerID", "KMeansCluster"]].to_string(index=False))

    # Plot an elbow curve for visual comparison.
    ks = list(range(2, max_k + 1))
    plt.figure()
    plt.plot(ks, inertias, marker="o")
    plt.title("K-Means Elbow Curve")
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("Inertia")
    plt.tight_layout()
    plt.savefig("elbow_curve.png")
    plt.close()

    # Plot clusters using income and spending score as the two displayed dimensions.
    plt.figure()
    for label in sorted(data["KMeansCluster"].unique()):
        group = data[data["KMeansCluster"] == label]
        plt.scatter(group["AnnualIncome"], group["SpendingScore"], label=f"Cluster {label}")
    plt.title("Customer Segments (K-Means)")
    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.legend()
    plt.tight_layout()
    plt.savefig("customer_clusters.png")
    plt.close()
    return data


def other_models(data, scaled):
    """Compare DBSCAN and hierarchical clustering labels."""
    dbscan = DBSCAN(eps=1.25, min_samples=2)
    data["DBSCANCluster"] = dbscan.fit_predict(scaled)
    hierarchical = AgglomerativeClustering(n_clusters=3)
    data["HierarchicalCluster"] = hierarchical.fit_predict(scaled)
    print("\nModel label comparison:")
    print(data[["CustomerID", "KMeansCluster", "DBSCANCluster",
                "HierarchicalCluster"]].to_string(index=False))
    for column in ["KMeansCluster", "DBSCANCluster", "HierarchicalCluster"]:
        labels = data[column]
        unique = set(labels)
        # Silhouette score needs at least two labels and fewer labels than samples.
        if len(unique) > 1 and len(unique) < len(data):
            try:
                score = silhouette_score(scaled, labels)
                print(f"{column} silhouette score: {score:.3f}")
            except ValueError:
                print(f"{column}: silhouette score could not be calculated.")
        else:
            print(f"{column}: silhouette score not meaningful for these labels.")
    data.to_csv("segmented_customers.csv", index=False)
    print("\nSaved segmented_customers.csv, elbow_curve.png, and customer_clusters.png.")
    print("\nExample business insight: compare average income and spending by K-Means cluster.")
    print(data.groupby("KMeansCluster")[["Age", "AnnualIncome", "SpendingScore"]]
          .mean().round(1).to_string())


def main():
    """Load data, run analyses, and report output files."""
    data, scaled = load_customers()
    print(f"Loaded {len(data)} customers from {DATA_FILE.name}.")
    data = kmeans_analysis(data, scaled)
    other_models(data, scaled)


if __name__ == "__main__":
    main()
