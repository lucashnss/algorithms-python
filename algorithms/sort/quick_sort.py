import random
import time

def partition(list,begin,end):
    pivot = list[end]
    i = begin
    for j in range(begin,end):
        if list[j] <= pivot:
            list[j],list[i] = list[i],list[j]
            i += 1
    
    list[i],list[end] = list[end],list[i]
    return i

def quickSort(list,begin=0,end=None):
    if end == None:
        end = len(list)-1
    
    if begin < end:
        p = partition(list,begin,end)
        quickSort(list,begin,p-1)
        quickSort(list,p+1,end)

    return list


random_arr = random.sample(range(1,3000001),3000000)

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
    resultado = quickSort(random_arr)
    end_time = time.time()
    execution_time = end_time - start_time
    print(resultado)
    print(execution_time)