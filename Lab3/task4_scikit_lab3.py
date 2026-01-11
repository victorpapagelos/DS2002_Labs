import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans as SKKMeans
from sklearn.metrics import accuracy_score
from time import perf_counter


data = pd.read_csv("iris_train.csv")
x = data.drop(columns=['class']).values # drop classes so we have only features inside x
y = data['class'].values # y stores classes

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2) # train test split

start = perf_counter() # timer start

knn = KNeighborsClassifier(n_neighbors=3) # determine K value
knn.fit(x_train, y_train) # store data
knn_predictions = knn.predict(x_test) # predict classes

end = perf_counter() # timer end

knn_accuracy = accuracy_score(y_test, knn_predictions) * 100 #calculate accuracy
print(f"KNN Scikit-Learn Accuracy: {knn_accuracy:.2f}%") #print with 2 decimals
print("KNN Predictions (first 10 points):", knn_predictions[:10]) # print first 10 points (classes/labels)

print(f"time: {end - start} seconds\n") # calculate time elapsed

x_all = x

start = perf_counter()

kmeans_skl = SKKMeans(n_clusters=3, random_state=2)
kmeans_skl.fit(x_all)

end = perf_counter()

cluster_labels = kmeans_skl.labels_
centroids = kmeans_skl.cluster_centers_

print("K-Means Cluster assignments (first 10 points):", cluster_labels[:10])
print("K-Means Centroids:\n", centroids)

print(f"time: {end - start} seconds")