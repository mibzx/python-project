# Project Report: Customer Segmentation

**Student name:** ____________________  
**Roll number:** ____________________  
**Course:** MCA III Semester — Python Programming

## 1. Abstract
Customer segmentation groups customers with similar features. This project standardises age, annual income, and spending score, then compares K-Means, DBSCAN, and hierarchical clustering. It creates plots and a CSV containing cluster labels.

## 2. Problem statement
A business may want to understand different customer profiles to plan communication and services. Clustering can help explore patterns in customer data without pre-labelled categories.

## 3. Objectives
- Load and inspect a customer dataset.
- Standardise numerical features.
- Apply multiple clustering methods.
- Use inertia and silhouette score as evaluation aids.
- Visualise groups and summarise their average profiles.
- Provide an optional Streamlit dashboard.

## 4. Tools and concepts
Python, pandas, scikit-learn, matplotlib, standardisation, unsupervised learning, K-Means, DBSCAN, agglomerative clustering, and silhouette score.

## 5. Methodology
1. Read `customers.csv`.
2. Select Age, AnnualIncome, and SpendingScore.
3. Standardise the selected columns.
4. Fit K-Means for multiple cluster counts and print inertia/silhouette scores.
5. Use k=3 for the demonstration and plot an elbow curve.
6. Fit DBSCAN and agglomerative clustering for comparison.
7. Save cluster labels and calculate mean feature values by K-Means cluster.

## 6. Evaluation
The silhouette score measures how similar a point is to its own cluster compared with other clusters; values closer to 1 generally indicate better separation, values around 0 indicate overlap, and negative values may indicate poor assignment. DBSCAN can label points as noise (`-1`), so interpret its score carefully. No single metric alone proves a model is best.

## 7. Dataset
The included 20-row dataset is synthetic and created only to demonstrate the pipeline. It is not representative of a real market.

## 8. Testing
Run `python main.py` and verify the printed scores and generated files. Run `streamlit run app.py` to test the cluster-count slider and CSV download. Record actual observations and include your own screenshots.

## 9. Limitations
The dataset is tiny and synthetic. The selected K=3 is a demonstration choice, not a universal optimum. Clustering depends on feature choice, scaling, and algorithm parameters.

## 10. Conclusion
The project demonstrates a basic unsupervised-learning workflow, model comparison, visualisation, and business-profile summaries.

## 11. Future scope
Use a larger authorised dataset, add better data cleaning, compare more clustering parameters, and validate findings with domain experts.
