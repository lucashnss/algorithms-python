import random
import time

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))

    return newArr


random_arr = random.sample(range(1,50001),50000)

repeated = [1,1,1,1,7,7,7,7,7,5,2,0,3,9,11,19,36,23,7,9]

repeated_sorted = [1,1,1,1,1,1,2,2,2,2,3,3,4,4,6,11,15,20,35]

sorted = [1,5,9,13,18,25,29,35,49,70,100,150,170]

reversed_sorted = [170,150,133,100,70,50,33,25,11,5,2]

reversed_repeated = [100,70,70,70,70,65,61,61,61,61,61,55,55,55,55,43,37,25,13,5]

lexicographic = ['ceça','breno','carlos','felipe','lucas','paulo','leopoldo','murilo']
                 
lexicographic_ordered = ['ana','beatriz','breno','carlos','eduardo','lucas','ester','murilo']

if __name__ == "__main__":
    item = 'lucas'
    print(random_arr)
    start_time = time.time()
    resultado = selectionSort(random_arr)
    end_time = time.time()
    print(resultado)
    execution_time = end_time - start_time
    print(execution_time)
