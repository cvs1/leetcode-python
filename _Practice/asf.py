import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from knn_classifier import knn_predict
import numpy as np
from collections import Counter


# Calculating the Euclidean distance between two points
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))


# Vectorized approach to find the k-nearest neighbors
def find_k_nearest(x_train, y_train, test_point, k=5):
    # Computing distances vectorized
    distances = np.sqrt(np.sum((x_train - test_point) ** 2, axis=1))
    # Geting indices of k smallest distances
    k_indices = np.argsort(distances)[:k]
    # Retrieving labels of k-nearest neighbors
    k_nearest_labels = y_train[k_indices]
    # Finding the most common label
    most_common = Counter(k_nearest_labels).most_common(1)
    return most_common[0][0]


# Predicting the label for each test instance based on k-nearest neighbors
def knn_predict(x_train, y_train, x_test, k=5):
    label_predictions = [find_k_nearest(x_train, y_train, test_point, k) for test_point in x_test]
    return np.array(label_predictions)


# Loading  the test and train data
training_dataset = pd.read_csv('/Users/cvs/Desktop/training_data.txt', header=None, delimiter=',')
test_dataset = pd.read_csv('/Users/cvs/Desktop/test_data.txt', header=None, delimiter=',')

# Prepare the feature and label data from training_data
features_train = training_dataset.iloc[:, :-1].values
Y_train = training_dataset.iloc[:, -1].values
X_test = test_dataset.values


# Plotting the function Visualization function for prediction outcomes
def visualize_predictions(neighbors, X_test, outcome):
    plt.figure(figsize=(8, 6))
    plt.scatter(X_test[outcome == 0, 0], X_test[outcome == 0, 1], color='yellow', label='Class 0 yellow')
    plt.scatter(X_test[outcome == 1, 0], X_test[outcome == 1, 1], color='red', label='Class 1 red')
    plt.title(f'Visualization of Test Data Set with k={neighbors}')
    plt.xlabel('Attribute 1')
    plt.ylabel('Atrribute 2')
    plt.grid(True)
    plt.legend()
    plt.show()


# Executing the Prediction and ploting and visulalization for different k values
k_values = [5, 10, 15]
for neighbors in k_values:
    predicted_labels = knn_predict(features_train, Y_train, X_test, neighbors)
    visualize_predictions(neighbors, X_test, predicted_labels)
