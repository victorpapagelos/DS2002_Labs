import csv
import numpy as np
from time import perf_counter

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

class KNN_Numpy:
    def __init__(self, k):
        self.k = k

    def fit(self, features_train, labels_train):
        self.features_train = features_train
        self.labels_train = labels_train

    def predict_multiple(self, features_test):
        predictions = []

        for element_test in features_test:
            prediction = self.predict(element_test)
            predictions.append(prediction)
        return predictions


    def predict(self, new_element):
            
        distances = (np.sum((self.features_train - new_element) ** 2, axis=1)) ** 0.5

        k_indices = np.argpartition(distances, self.k)[:self.k]

        labels = {}

        for i in k_indices:
            label = self.labels_train[i]
            if label in list(labels.keys()):
                labels[label] += 1
            else:
                labels[label] = 1

        most_common_label = list(labels.keys())[0]
        for label in labels:
            if labels[label] > labels[most_common_label]:
                most_common_label = label

        return most_common_label


features_train, labels_train = load("iris_train.csv")
features_test, labels_test = load("iris_test.csv")




start = perf_counter()

knn_np = KNN_Numpy(2)
knn_np.fit(features_train, labels_train)
predictions_np = knn_np.predict_multiple(features_test)

end = perf_counter()

accuracy = np.mean(predictions_np == labels_test) * 100

print(f"time: {end - start} seconds")
print(f"Accuracy: {accuracy}%")