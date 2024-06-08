import random
import time

def merge(arr,begin,mid,end):
    left = arr[begin:mid]
    right = arr[mid:end]
    top_left,top_right = 0,0
    for k in range(begin,end):
        if top_left >= len(left):
            arr[k] = right[top_right]
            top_right += 1
        elif top_right >= len(right):
            arr[k] = left[top_left]
            top_left += 1
        elif left[top_left] < right[top_right]:
            arr[k] = left[top_left]
            top_left += 1
        else:
            arr[k] = right[top_right]
            top_right += 1
    
    return arr

def mergeSort(arr,begin=0,end=None):
    if end == None:
        end = len(arr)
    if (end - begin) > 1:
        mid = (end + begin)//2
        mergeSort(arr,begin,mid)
        mergeSort(arr,mid,end)
        merge(arr,begin,mid,end)
    return arr

random_arr = random.sample(range(1,1001),1000)

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
    resultado = mergeSort(random_arr)
    end_time = time.time()
    execution_time = end_time - start_time
    print(resultado)
    print(execution_time)