"""Optional Streamlit dashboard for the Customer Segmentation project."""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from pathlib import Path

st.set_page_config(page_title="Customer Segmentation", layout="wide")
st.title("Customer Segmentation Dashboard")
st.write("Explore customer groups using age, annual income, and spending score.")

data_path = Path(__file__).with_name("customers.csv")
data = pd.read_csv(data_path)
k = st.slider("Number of K-Means clusters", min_value=2, max_value=6, value=3)

features = data[["Age", "AnnualIncome", "SpendingScore"]]
scaled = StandardScaler().fit_transform(features)
model = KMeans(n_clusters=k, random_state=42, n_init=10)
data["Cluster"] = model.fit_predict(scaled)

st.subheader("Customer data with cluster labels")
st.dataframe(data, use_container_width=True)

fig, ax = plt.subplots()
for label in sorted(data["Cluster"].unique()):
    group = data[data["Cluster"] == label]
    ax.scatter(group["AnnualIncome"], group["SpendingScore"], label=f"Cluster {label}")
ax.set_xlabel("Annual Income")
ax.set_ylabel("Spending Score")
ax.set_title("Income vs Spending Score")
ax.legend()
st.pyplot(fig)

st.subheader("Average profile by cluster")
st.dataframe(data.groupby("Cluster")[["Age", "AnnualIncome", "SpendingScore"]].mean().round(1))
st.download_button("Download segmented CSV", data.to_csv(index=False), "segmented_customers.csv", "text/csv")
