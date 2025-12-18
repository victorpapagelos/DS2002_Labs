import numpy as np
from time import perf_counter
import csv

def load(filename):
    features = []
    labels = []
 
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            features.append(row[:-1])
            labels.append(row[-1])
        
        for i in range(len(features)):
            for j in range(len(features[i])):
                features[i][j] = float(features[i][j])
    return (np.array(features), np.array(labels))

class KMeans:
    def __init__(self, k):
        self.k = k

    def fit(self, cluster_features):
        self.cluster_features = cluster_features
        self.cluster_centers = cluster_features[:self.k]

    def assign_clusters(self):
        cluster_distances = []
        clusters = []
        
        #calculate the distance
        for i in range(self.k):
            clusters.append([])

            cluster_center = self.cluster_centers[i]
            cluster_distances.append((np.sum((self.cluster_features - cluster_center) ** 2, axis=1)) ** 0.5) 

        for i in range(len(self.cluster_features)):
            closest = 0

            for j in range(self.k):
                if cluster_distances[closest][i] > cluster_distances[j][i]:
                    closest = j

            clusters[closest].append(i)
        return clusters

    def calculate_centers(self, clusters):
        new_cluster_centers = []
        for i in range(self.k):
            features = np.zeros(shape=(len(clusters[i]), len(self.cluster_features[0])), dtype=float) 
            # Y = cluster amount, X = feature amount
            
            for j in range(len(clusters[i])):
                features[j] = self.cluster_features[clusters[i][j]]

            # Calculate
            new_cluster_centers.append(np.mean(features,axis=0))

            pass
        return np.array(new_cluster_centers)     

    def run(self, steps):
        for i in range(steps):
            clusters = self.assign_clusters()
            new_centers = self.calculate_centers(clusters)

            if ((np.array(new_centers) == np.array(self.cluster_centers)).all()):
                print(f'Finished after {i} steps.\nCenters: \n{new_centers}')
                break
            self.cluster_centers = new_centers



cluster_features, cluster_labels = load("iris.csv")

start = perf_counter()

k = KMeans(2)
k.fit(cluster_features)
k.run(100)

end = perf_counter()

print(f"time: {end - start} seconds")