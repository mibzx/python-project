# 6. Customer Segmentation

## Aim
Group customers with similar characteristics using clustering algorithms and explore the segments visually.

## Requirements
Python 3.10+ and packages in `requirements.txt`.

## Install and run
```bash
pip install -r requirements.txt
python main.py
```
Optional interactive dashboard:
```bash
streamlit run app.py
```

## Included data
`customers.csv` is a small synthetic sample for coursework, not real customer data.

## Features
- Preprocessing and standardisation.
- K-Means with inertia/elbow values and silhouette scores for multiple K values.
- DBSCAN and hierarchical/agglomerative clustering comparison.
- Cluster visualisation and business-profile summary.
- Exports `segmented_customers.csv`, `elbow_curve.png`, and `customer_clusters.png`.
- Optional Streamlit dashboard with selectable K and CSV download.

## Interpretation
Cluster numbers are arbitrary labels, not rankings. The sample is small and synthetic; do not make real business decisions from it. The elbow curve is a heuristic, and DBSCAN's result depends on its parameters.
