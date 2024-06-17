import numpy as np 
from collections import Counter
from kNN_regression import euclidean_distance

def kNN_classifier(train_data,train_labels,test_point,k):
    distances = []
    for i in range(len(train_data)):
        dist = euclidean_distance(train_data[i],test_point)
        distances.append((dist,train_labels[i]))
    distances.sort(key=lambda x:x[0])
    nearest_neighbors = distances[:k]
    nearest_labels = [label for _,label in nearest_neighbors]
    most_common = Counter(nearest_labels).most_common(1)
    return most_common[0][0]


if __name__ == "__main__":
    train_data = np.array([[1,2],[2,3],[3,4],[6,7]])
    train_labels = np.array(['A','A','B','B'])
    test_point = np.array([4,5])
    k = 3
    result = kNN_classifier(train_data,train_labels,test_point,k)
    print(f"The class of the test point is {result}")