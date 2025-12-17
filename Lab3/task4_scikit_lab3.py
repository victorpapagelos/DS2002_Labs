import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans as SKKMeans
from sklearn.metrics import accuracy_score


data = pd.read_csv("iris_train.csv")
X = data.drop(columns=['class']).values#features
y = data['class'].values#labels

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
knn_predictions = knn.predict(X_test)

knn_accuracy = accuracy_score(y_test, knn_predictions) * 100
print(f"KNN Scikit-Learn Accuracy: {knn_accuracy:.2f}%")
print("KNN Predictions (first 10 points):", knn_predictions[:10])

X_all = X

kmeans_skl = SKKMeans(n_clusters=3, random_state=2)
kmeans_skl.fit(X_all)

cluster_labels = kmeans_skl.labels_
centroids = kmeans_skl.cluster_centers_

print("K-Means Cluster assignments (first 10 points):", cluster_labels[:10])
print("K-Means Centroids:\n", centroids)

