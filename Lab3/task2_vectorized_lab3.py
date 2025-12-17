
from collections import Counter
from sklearn.model_selection import train_test_split
import math
import csv
import numpy as np
import time

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

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 2)

x_train = np.array(x_train)
x_test = np.array(x_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

def euclidean_distance(a, b):
    return math.sqrt(sum((an - bn) ** 2 for an, bn in zip(a, b)))

class KNN_Numpy:
    def __init__(self, k):
        self.k = k

    def fit(self, x, y):
        self.x_train = x
        self.y_train = y

    def predict(self, x_test):
        predictions = []

        for x in x_test:

            distances = np.sqrt(np.sum((self.x_train - x) ** 2, axis=1))

            k_indices = np.argsort(distances)[:self.k]

            k_labels = self.y_train[k_indices]
            most_common = Counter(k_labels).most_common(1)[0][0]
            predictions.append(most_common)
            print("Precicted class:", most_common)
        return predictions

knn = KNN_Numpy(2)
knn.fit(x_train, y_train)
predictions = knn.predict(x_test)
accuracy = np.mean(predictions == y_test) * 100

start = time.time()
knn_np = KNN_Numpy(2)
knn_np.fit(x_train, y_train)
predictions_np = knn_np.predict(x_test)
end = time.time()

print(f"time: {end - start} seconds")
print(f"Accuracy: {accuracy}%")

#plot
import matplotlib.pyplot as plt

# Assume x_test (NumPy array) and predictions_np (list or array) exist
colors = {'Iris-setosa':'red', 'Iris-versicolor':'green', 'Iris-virginica':'blue'}

plt.figure(figsize=(6,5))
for point, label in zip(x_test, predictions_np):
    plt.scatter(point[0], point[1], color=colors[label], alpha=0.6)

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Task 2: Vectorized KNN Predictions")
plt.show()
