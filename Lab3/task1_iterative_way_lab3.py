import csv
from time import perf_counter

def load(filename):
    features = []
    labels = []
 
    with open(filename, "r") as file: 
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            features.append(row[:-1]) # Do not add labels.
            labels.append(row[-1]) # Add only labels.
                                    # element -1 in row is the label


        for i in range(len(features)):          # Per row
            for j in range(len(features[i])):   # Per feature in the row.
                features[i][j] = float(features[i][j])  # Make each element in the row a float instead of a string
    return (features, labels) # tuple

class KNN:
    def __init__(self, k=3):
        self.k = k 

    def euclidean_distance(self, A, B):
        result = 0.0
        for i in range(len(A)): # len(A) amount of features 
            result += (A[i] - B[i]) ** 2

        return result ** 0.5

    def fit(self, features_train, labels_train): # Give the model access to the necessary values by storing them as object variables
        self.features_train = features_train
        self.labels_train = labels_train

    def predict_multiple(self, features_test):
        predictions = []                        # Storage
        for element in features_test:       # for each test row
            prediction = self.predict(element)  # Predicts each element
            predictions.append(prediction)      # Puts them in storage 
        return predictions

    def predict(self, new_element):
        distances:list[tuple[float,str]] = []  # (distance, label)          
        for i in range(len(self.features_train)): # Runs once for every training data with the current one being i
            element_feature = self.features_train[i] # gets the features for element i
            element_label = self.labels_train[i]     # gets the label for element i

            distance = self.euclidean_distance(new_element, element_feature) # Gets the distance between new_element and element_feature (element_feature is the features for element i)
            distances.append((distance, element_label)) # Add a tuple with distance and element_label so you can sort the distance and keep track of the element_labels

        distances.sort() # Sort it, magically sort its by distance.

        k_nearest_labels = []
        for j in range(self.k):
            k_nearest_labels.append(distances[j][1]) # Adds the 3 lowest valeus of the sorted distances list.
                                                     # [1] is the element_label part of the tuple on line 51

        labels = {}
        for label in k_nearest_labels:       # for each of our nearest labels 
            if label in list(labels.keys()):   # check if the label is already in our labels dict
                labels[label] += 1             # add to it
            else:
                labels[label] = 1              # add

        most_common_label = list(labels.keys())[0] # Assumes the base label is 0
        for label in labels:                       # checks each label in the labels dict
            if labels[label] > labels[most_common_label]: # If we have more of label than the most common one
                most_common_label = label                 # then we make label our new most common one

        return most_common_label # return the most common label



features_train, labels_train = load("iris_train.csv") # Loading using tuples 
features_test, labels_test = load("iris_test.csv") # Loading using tuples

start = perf_counter()

knn = KNN(k=7)
knn.fit(features_train, labels_train)
predictions = knn.predict_multiple(features_test)

end = perf_counter()

correct = 0
for i in range(len(labels_test)): # For each test element
    if predictions[i] == labels_test[i]: # Is the predicted element correct?
        correct += 1                     # If it is correct, then add one to our tracker.
accuracy = correct / len(labels_test) * 100 # Gets the accuracy, if you get 25/50 correct you get back 50.

print(f"time: {end - start} seconds")
print(f"Accuracy: {accuracy:.2f}%")