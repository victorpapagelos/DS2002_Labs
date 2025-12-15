import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.model_selection import train_test_split

data = pd.read_csv("iris_train.csv")

x = data.drop(columns=['class']).values
y = data['class'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 2)

#plt.scatter(x_train[y_train == 'Iris-virginica', 0], x_train[y_train == 'Iris-virginica', 1], color='tab:green', label='Iris-virginica')
#plt.scatter(x_train[y_train == 'Iris-setosa', 0], x_train[y_train == 'Iris-setosa', 1], color='tab:red', label='Iris-setosa')
#plt.scatter(x_train[y_train == 'Iris-versicolor', 0], x_train[y_train == 'Iris-versicolor', 1], color='tab:blue', label='Iris-versicolor')
#plt.xlabel('sepal_length')
#plt.ylabel('petal_width')
#plt.legend()
#plt.show

plt.plot([1,2,3], [4,5,6])
plt.show()

import os
print(os.getcwd())