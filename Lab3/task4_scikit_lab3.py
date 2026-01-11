import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans as SKKMeans
from sklearn.metrics import accuracy_score
from time import perf_counter

# import own versions
from task1_iterative_way_lab3 import KNN
from task3_Kmeans_vectorized_lab3 import KMeans


data = pd.read_csv("iris_train.csv")
x = data.drop(columns=['class']).values # drop classes so we have only features inside x
y = data['class'].values # y stores classes

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2) # train test split

SKKNstart = perf_counter() # timer start

knn = KNeighborsClassifier(n_neighbors=3) # determine K value
knn.fit(x_train, y_train) # store data
knn_predictions = knn.predict(x_test) # predict classes

SKKNend = perf_counter() # timer end

knn_accuracy = accuracy_score(y_test, knn_predictions) * 100 #calculate accuracy
print(f"__________\nKNN Scikit-Learn Accuracy: {knn_accuracy:.2f}%\n__________\n") #print with 2 decimals
print("KNN Predictions (first 10 points):", knn_predictions[:10]) # print first 10 points (classes/labels)

print(f"\nSCIKIT KNN time: {SKKNend - SKKNstart} seconds\n") # calculate time elapsed

x_all = x # use all features for k-means

skkmeansstart = perf_counter() # timer

kmeans_skl = SKKMeans(n_clusters=4, random_state=2) # create clusters
kmeans_skl.fit(x_all) # assign points to clusters + finds centers

skkmeansend = perf_counter() # timer

cluster_labels = kmeans_skl.labels_
centroids = kmeans_skl.cluster_centers_

print("SKK-Means Cluster assignments (first 10 points):", cluster_labels[:10])
print("SKK-Means Centroids:\n", centroids)

print(f"SKK-Means time: {skkmeansend - skkmeansstart} seconds")


#run own versions and compare time


#Task 1

import csv
import numpy as np

def load(filename):
    features = [] # empty lists containing features & labels
    labels = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        for row in reader:
            features.append(row[:-1])  # feature values
            labels.append(row[-1])     # class labels

    # converts feature values to float
    for i in range(len(features)): # through each datapoint
        for j in range(len(features[i])): # each feature
            features[i][j] = float(features[i][j]) # convert features value from string to float

    return features, labels #return values

features_train, labels_train = load("iris_train.csv") #load training data
features_test, labels_test = load("iris_test.csv") #load test data

ownknnstart = perf_counter() #timer start

knn = KNN(k=4) #determine K value
knn.fit(features_train, labels_train) # store training data
predictions = knn.predict_multiple(features_test) #predict labels for all test data

ownknnend = perf_counter() #timer end

correct = 0
for i in range(len(labels_test)):
    if predictions[i] == labels_test[i]: # calculate accuracy
        correct += 1

accuracy = correct / len(labels_test) * 100 # percentage of accurate predictions

print(f"time: {ownknnend - ownknnstart} seconds") # prints time elapsed
print(f"Accuracy: {accuracy:.2f}%") #accuracy


#Task 3

data_features, data_labels = load("iris.csv") # load dataset

ownkmeansstart = perf_counter() # timer start

kmeans = KMeans(4) # amount of clusters
kmeans.fit(data_features) # fit data (assign)
clusters, centers = kmeans.run(100) # run up to 100 times (max_steps)

ownkmeansend = perf_counter() # timer end

print("Cluster centers:\n", centers) # print centers
for i in range(kmeans.k):
    print(f"Cluster {i} points indices:", clusters[i]) # prints cluster indexes
print(f"time: {ownkmeansend - ownkmeansstart} seconds") # time elapsed



#TIME COMPARISON
print("\nOperation time comparison:\n")
print("SCIKIT LEARN OPERATION TIMES:")
print(f"SKK-Means time: {skkmeansend - skkmeansstart} seconds")
print(f"SCIKIT KNN time: {SKKNend - SKKNstart} seconds")

print("\nOWN VERSIONS OPERATION TIME (TASK 1 & 3)")
print(f"OWN KNN time: {ownknnend - ownknnstart} seconds")
print(f"OWN KMEANS time: {ownkmeansend - ownkmeansstart} seconds")