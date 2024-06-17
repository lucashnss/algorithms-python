import numpy as np

def euclidean_distance(point1,point2):
    return np.sqrt(np.sum((point1-point2)**2))

def kNN_regression(train_data,train_labels,test_point,k):
    distances = []
    for i in range(len(train_data)):
        dist = euclidean_distance(train_data[i],test_point)
        distances.append((dist,train_labels[i]))
    distances.sort(key=lambda x:x[0])
    nearest_neighbors = distances[:k]
    nearest_values = [value for _,value in nearest_neighbors]
    return np.mean(nearest_values)

if __name__ == "__main__":
    train_data = np.array([[1,2],[2,3],[3,4],[6,7]])
    train_labels = np.array([1.0,2.0,3.0,6.0])
    test_point = np.array([4,5])
    k = 3
    result = kNN_regression(train_data,train_labels,test_point,k)
    print(f"The predicted value of the test point is {result}")