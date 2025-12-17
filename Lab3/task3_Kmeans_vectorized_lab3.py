import csv
import random

x = []
y = []

with open("iris_train.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        features = list(map(float, row[:-1]))
        label = row[-1]

        x.append(features)
        y.append(label)

X_all = x + [] 

class KMeans:
    def __init__(self, k=3, max_iters=100, tol=1e-6):
        self.k = k
        self.max_iters = max_iters
        self.tol = tol

    def distance(self, point1, point2):
        #euclidean distance
        return sum((a - b) ** 2 for a, b in zip(point1, point2)) ** 0.5

    def fit(self, X):

        self.centroids = random.sample(X, self.k)
        for i in range(self.max_iters):
            clusters = [[] for _ in range(self.k)]

            for point in X:
                distances = [self.distance(point, c) for c in self.centroids]
                min_index = distances.index(min(distances))
                clusters[min_index].append(point)

            new_centroids = []
            for cluster in clusters:
                if cluster:
                    avg = [sum(features)/len(features) for features in zip(*cluster)]
                    new_centroids.append(avg)
                else:
                    new_centroids.append(random.choice(X))

            diff = sum(self.distance(a, b) for a, b in zip(self.centroids, new_centroids))
            if diff < self.tol:
                break

            self.centroids = new_centroids

        self.labels = []
        for point in X:
            distances = [self.distance(point, c) for c in self.centroids]
            self.labels.append(distances.index(min(distances)))

        return self.labels

kmeans = KMeans(k=3)
cluster_labels = kmeans.fit(X_all)

print("Cluster assignments (first 10 points):", cluster_labels[:10])
print("Centroids:", kmeans.centroids)
