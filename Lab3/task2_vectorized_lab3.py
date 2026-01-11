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

class KNN_Numpy:
    def __init__(self, k): # constructor, k = amount of neighbours to check
        self.k = k

    def fit(self, features_train, labels_train): #no training needed, stores data inside objects to be used later
        self.features_train = features_train
        self.labels_train = labels_train

    def predict_multiple(self, features_test): #predicts class for multiple points
        predictions = [] # list for predictions
        for element in features_test: 
            predictions.append(self.predict(element)) # use predict function to get label, store in the list
        return predictions #return list

    def predict(self, new_element): # unseen data point
        # calculate distance to all training points (euclidean distance)
        distances = np.sqrt(np.sum((self.features_train - new_element) ** 2, axis=1))

        # get index of K closest training points
        k_indices = np.argsort(distances)[:self.k] #sort distances, grab up until index value of K

        # count labels
        label_count = {} #stores label (keys) & appearances (values)
        for i in k_indices: #loops through labels
            label = self.labels_train[i]
            if label in label_count:
                label_count[label] += 1 #if already in dictionary, +1 count
            else:
                label_count[label] = 1 #if not seen, add to dic

        # find most common label
        most_common_label = list(label_count.keys())[0] #pick first label (start point)
        for label in label_count: # loop through labels
            if label_count[label] > label_count[most_common_label]: # if current label count is greater than "start point"
                most_common_label = label # replace with new label

        return most_common_label # return label





features_train, labels_train = load("iris_train.csv") # load training data
features_test, labels_test = load("iris_test.csv") # load test data

start = perf_counter() # timer start

knn_np = KNN_Numpy(4) # determine K value
knn_np.fit(features_train, labels_train) # store training data 
predictions_np = knn_np.predict_multiple(features_test) # predicts labels for all test data

end = perf_counter() # timer end

accuracy = np.mean(predictions_np == labels_test) * 100 # calculate accuracy

print(f"time: {end - start} seconds") # print time elapsed
print(f"Accuracy: {accuracy:.2f}%") # accuracy
