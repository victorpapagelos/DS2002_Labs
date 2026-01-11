import csv
from time import perf_counter

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


class KNN:
    def __init__(self, k=0): #constructor, k = amount of neighbours to check
        self.k = k

    def euclidean_distance(self, A, B): #euclidean distance
        total = 0.0 #distance value
        for i in range(len(A)):
            total += (A[i] - B[i]) ** 2 
        return total ** 0.5 #takes square root of total (the difference, squared)

    def fit(self, features_train, labels_train): #no training needed, stores data inside objects to be used later
        self.features_train = features_train
        self.labels_train = labels_train

    def predict_multiple(self, features_test): #predicts class for multiple points
        predictions = [] # list for predictions
        for element in features_test: 
            predictions.append(self.predict(element)) # predict function to get label, store in the list
        return predictions #return list

    def predict(self, new_element): # the unseen data point
        distances = [] # stores distances

        # calculate distance to all training points
        for i in range(len(self.features_train)): #for each training data point
            distance = self.euclidean_distance(new_element, self.features_train[i])
            distances.append((distance, self.labels_train[i]))

        # sort by distance (low to high)
        distances.sort()

        k_nearest_labels = []
        for i in range(self.k): #our k value
            k_nearest_labels.append(distances[i][1]) #take labels from k nearest points

        # count labels
        label_count = {} #stores label (key) & value (appearances)
        for label in k_nearest_labels: #loops through labels
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


features_train, labels_train = load("iris_train.csv") #load training data
features_test, labels_test = load("iris_test.csv") #load test data

start = perf_counter() #timer start

knn = KNN(k=7) #determine K value
knn.fit(features_train, labels_train) # store training data
predictions = knn.predict_multiple(features_test) #predict labels for all test data

end = perf_counter() #timer end

correct = 0
for i in range(len(labels_test)):
    if predictions[i] == labels_test[i]: # calculate accuracy
        correct += 1

accuracy = correct / len(labels_test) * 100 # percentage of accurate predictions

print(f"time: {end - start} seconds") # prints time elapsed
print(f"Accuracy: {accuracy:.2f}%") #accuracy
