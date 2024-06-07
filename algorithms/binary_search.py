def binary_search(list,item, ascending=True,max=None,min=0):
    if max is None:
            max = len(list)-1

    mid = (min+max)//2

    if min > max:
        return None

    if item == list[mid]:
        return mid
    
    if ascending:
        if item > list[mid]:
            return binary_search(list,item,True,max,mid+1)
        else:
            return binary_search(list,item,True,mid-1,min)
    
    else:
        if item < list[mid]:
            return binary_search(list,item,False,max,mid+1)
        else:
            return binary_search(list,item,False,mid-1,min)



repeated = [1,1,1,1,1,1,2,2,2,2,3,3,4,4,6,11,15,20,35]

sorted = [1,5,9,13,18,25,29,35,49,70,100,150,170]

reversed = [100,70,50,33,25,11,5,2]

reversed_repeated = [100,70,70,70,70,65,61,61,61,61,61,55,55,55,55,43,37,25,13,5]

lexicographic_ordered = ['ana','beatriz','breno','carlos','eduardo','lucas','ester','murilo']

if __name__ == "__main__":
    item = 'lucas'
    resultado = binary_search(lexicographic_ordered,item,True)
    print(resultado)
