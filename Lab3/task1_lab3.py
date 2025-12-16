import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.model_selection import train_test_split
import math

data = pd.read_csv("iris_train.csv")

x = data.drop(columns=['class']).values.tolist()
y = data['class'].values.tolist()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 2)

def euclidean_distance(a, b):
    return math.sqrt(sum((an - bn) ** 2 for an, bn in zip(a, b)))

class KNN:
    def __init__(self, k):
        self.k = k
    
    def fit(self, x, y):
        self.x_train = x
        self.y_train = y

    def predict(self, new_points):
        predictions = []
        for new_point in new_points:
            predictions.append(self.predict_class(new_point))
        return predictions
    
    def predict_class(self, new_point):
        distances = []

        for i in range(len(self.x_train)):
            d = euclidean_distance(self.x_train[i], new_point)
            distances.append([d, self.y_train[i]])

        distances.sort(key=lambda item: item[0])

        k_nearest_labels = []
        for i in range(self.k):
            k_nearest_labels.append(distances[i][1])

        most_common = Counter(k_nearest_labels).most_common(1)[0][0]
        return most_common
    
knn = KNN(1)
knn.fit(x_train, y_train)
predictions = knn.predict(x_test)
accuracy = sum(pred == true for pred, true in zip(predictions, y_test)) / len(y_test) * 100
print(f"Accuracy: {accuracy:.2f}%")