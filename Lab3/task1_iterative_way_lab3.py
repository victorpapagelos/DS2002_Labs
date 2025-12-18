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
    return (features, labels)

class KNN:
    def __init__(self, k=3):
        self.k = k

    def euclidean_distance(self, A, B):
        result = 0.0
        for i in range(len(A)):
            result += (A[i] - B[i]) ** 2

        return result ** 0.5

    def fit(self, features_train, labels_train):
        self.features_train = features_train
        self.labels_train = labels_train

    def predict_multiple(self, features_test):
        predictions = []
        for element in features_test:
            prediction = self.predict(element)
            predictions.append(prediction)
        return predictions

    def predict(self, new_element):
        distances = []
        for i in range(len(self.features_train)):
            element_feature = self.features_train[i]
            element_label = self.labels_train[i]

            distance = self.euclidean_distance(new_element, element_feature)
            distances.append((distance, element_label))

        distances.sort()

        k_nearest_labels = []
        for j in range(self.k):
            k_nearest_labels.append(distances[j][1])

        labels = {}
        for label in k_nearest_labels:
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

knn = KNN(k=7)
knn.fit(features_train, labels_train)
predictions = knn.predict_multiple(features_test)

correct = 0
for i in range(len(labels_test)):
    if predictions[i] == labels_test[i]:
        correct += 1
accuracy = correct / len(labels_test) * 100
print(f"Accuracy: {accuracy:.2f}%")

