import random
import time

def bubbleSort(list):
    lenght = len(list)
    for i in range(lenght):
        for j in range(i+1,lenght):
            if list[j] < list[i]:
                list[j],list[i] = list[i],list[j]
    return list

random_arr = random.sample(range(1,10001),10000)

repeated = [1,1,1,1,7,7,7,7,7,5,2,0,3,9,11,19,36,23,7,9]

repeated_sorted = [1,1,1,1,1,1,2,2,2,2,3,3,4,4,6,11,15,20,35]

sorted = [1,5,9,13,18,25,29,35,49,70,100,150,170]

reversed_sorted = [170,150,133,100,70,50,33,25,11,5,2]

reversed_repeated = [100,70,70,70,70,65,61,61,61,61,61,55,55,55,55,43,37,25,13,5]

lexicographic = ['ceça','breno','carlos','felipe','lucas','paulo','leopoldo','murilo']
                 
lexicographic_ordered = ['ana','beatriz','breno','carlos','eduardo','lucas','ester','murilo']

if __name__ == "__main__":
    item = 'lucas'
    start_time = time.time()
    resultado = bubbleSort(lexicographic)
    end_time = time.time()
    execution_time = end_time - start_time
    print(resultado)
    print(execution_time)