import csv
import math
from collections import Counter
import matplotlib.pyplot as plt

x = []
y = []

with open("iris_train.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    for row in reader:
        features = [float(value) for value in row[:-1]]
        x.append(features)
        y.append(row[-1])

split_index = int(len(x) * 0.8)
x_train = x[:split_index]
y_train = y[:split_index]
x_test = x[split_index:]
y_test = y[split_index:]

def euclidean_distance(a, b):
    dist = 0
    for i in range(len(a)):
        dist += (a[i] - b[i]) ** 2
    return math.sqrt(dist)

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, x_train_data, y_train_data):
        self.x_train = x_train_data
        self.y_train = y_train_data

    def predict(self, x_test_data):
        predictions = []
        for i in range(len(x_test_data)):
            point = x_test_data[i]
            prediction = self.predict_point(point)
            predictions.append(prediction)
        return predictions

    def predict_point(self, point):
        distances = []
        for i in range(len(self.x_train)):
            train_point = self.x_train[i]
            label = self.y_train[i]
            dist = euclidean_distance(point, train_point)
            distances.append((dist, label))

        distances.sort(key=lambda x: x[0])

        k_nearest_labels = []
        for j in range(self.k):
            k_nearest_labels.append(distances[j][1])

        counter = Counter(k_nearest_labels)
        most_common = counter.most_common(1)[0][0]
        return most_common

knn = KNN(k=3)
knn.fit(x_train, y_train)
predictions = knn.predict(x_test)

correct = 0
for i in range(len(y_test)):
    if predictions[i] == y_test[i]:
        correct += 1
accuracy = correct / len(y_test) * 100
print(f"Accuracy: {accuracy:.2f}%")

