import random


def quicksort(array,left,right):
    if (left>right):
        return
    pivot = array[int((left+right)/2)]
    partitionIndex = partition(array,left,right,pivot)
    if partitionIndex == -1:
        return
    quicksort(array,left,partitionIndex-1)
    quicksort(array,partitionIndex,right)


def partition(array,left,right,pivot):
    if left == right:
        return -1
    while left<=right:
        while array[left]<pivot and left<=right:
            left +=1

        while array[right]>pivot and left<=right:
            right -=1

        if left<=right:
            swap(array,left,right)
            left +=1
            right -=1
    return left

def swap(array,left,right):
    temp = array[left]
    array[left] = array[right]
    array[right] = temp

my=[]
for x in range(0,100):
    num = random.randint(1,101)
    my.append(num)

print(my)
#my=[4,2,35,9,5,6,3]
arraySize = len(my)
quicksort(my,0,arraySize-1)
print(my)

