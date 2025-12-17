import pandas as pd
import random

data = pd.read_csv("iris_train.csv")
X_all = data.drop(columns=['class']).values.tolist()

class KMeans:
    def __init__(self, k=3, max_iterations=100, tolerance=1e-6):
        self.k = k
        self.max_iterations = max_iterations
        self.tolerance = tolerance

    def distance(self, point1, point2):
        return sum((a - b) ** 2 for a, b in zip(point1, point2)) ** 0.5

    def fit(self, X):
        self.centroids = random.sample(X, self.k)

        for i in range(self.max_iterations):
            clusters = [[] for i in range(self.k)]

            for point in X:
                distances = [self.distance(point, centroid) for centroid in self.centroids]
                closest_index = distances.index(min(distances))
                clusters[closest_index].append(point)

            new_centroids = []
            for cluster in clusters:
                if cluster:
                    centroid = [sum(features)/len(features) for features in zip(*cluster)]
                    new_centroids.append(centroid)
                else:
                    new_centroids.append(random.choice(X))

            total_movement = sum(self.distance(a, b) for a, b in zip(self.centroids, new_centroids))
            if total_movement < self.tolerance:
                break

            self.centroids = new_centroids

        self.labels = []
        for point in X:
            distances = [self.distance(point, centroid) for centroid in self.centroids]
            self.labels.append(distances.index(min(distances)))

        return self.labels

kmeans = KMeans(k=3)
cluster_labels = kmeans.fit(X_all)

print("cluster assignments (first 10 points) -", cluster_labels[:10])
print("centroids -", kmeans.centroids)
