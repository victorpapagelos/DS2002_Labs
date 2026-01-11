import csv
import numpy as np
from time import perf_counter


def load(filename):
    features = [] # empty lists containing features & labels
    labels = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header (column names)

        for row in reader:
            features.append(row[:-1])  # feature values
            labels.append(row[-1])     # class labels (last)

    # converts feature values to float
    for i in range(len(features)): # through each datapoint
        for j in range(len(features[i])): # each feature in each datapoint
            features[i][j] = float(features[i][j]) # convert features value from string to float

    return np.array(features), np.array(labels)  # convert to numpy arrays

class KMeans:
    def __init__(self, k):  # constructor, k = amount of clusters
        self.k = k

    def fit(self, data):
        self.data = np.array(data) # store data
        self.centers = data[:self.k] # starting cluster points using K

    def assign_clusters(self):
        clusters = [[] for _ in range(self.k)]  # create an empty list for each cluster

        for i in range(len(self.data)): # loop through eery data point
            # calculate distance from points to cluster center
            distances = np.sqrt(np.sum((self.centers - self.data[i]) ** 2, axis=1))
            closest_center = np.argmin(distances)  # np.argminn finds index of closest center
            clusters[closest_center].append(i)     # assign index to list

        return clusters

    def update_centers(self, clusters): # calculate new center
        new_centers = [] # empty list

        for i in range(self.k): # each cluster
            if len(clusters[i]) == 0:  # cluster has no points
                new_centers.append(self.centers[i])  # keep old center
            else:
                points = np.array([self.data[j] for j in clusters[i]])  # take all points
                new_centers.append(np.mean(points, axis=0))  # calculate mean

        return np.array(new_centers) # updated center


    def run(self, max_steps=100):
        clusters = [[] for _ in range(self.k)]  # create an empty list for each cluster

        for step in range(max_steps):
            clusters = self.assign_clusters()         # assign points
            new_centers = self.update_centers(clusters)  # update centers safely

        # check if cluster centers did not change
            if np.all(new_centers == self.centers): # if updated center = previous center
                print(f"Converged after {step} steps") # clusters are done / settled
                break

            self.centers = new_centers  # update centers

        return clusters, self.centers


data_features, data_labels = load("iris.csv") # load dataset

start = perf_counter() # timer start

kmeans = KMeans(4) # amount of clusters
kmeans.fit(data_features) # fit data (assign)
clusters, centers = kmeans.run(100) # run up to 100 times (max_steps)

end = perf_counter() # timer end

print("Cluster centers:\n", centers) # print centers
for i in range(kmeans.k):
    print(f"Cluster {i} points indices:", clusters[i]) # prints cluster indexes
print(f"time: {end - start} seconds") # time elapsed
