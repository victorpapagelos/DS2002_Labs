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
        cluster = []
        
        #calculate the distance
        for i in range(self.k):
            cluster.append([])

            cluster_center = self.cluster_centers[i]
            cluster_distances.append((np.sum((self.cluster_features - cluster_center) ** 2, axis=1)) ** 0.5) 

        for i in range(len(self.cluster_features)):
            closest = 0

            for j in range(self.k):
                if cluster_distances[closest][i] > cluster_distances[j][i]:
                    closest = j


                





cluster_features, cluster_labels = load("iris.csv")

k = KMeans(2)
k.fit(cluster_features)

