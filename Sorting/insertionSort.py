import random




def insertionSort(array, sizeOfArray):
    for k in range(1,sizeOfArray):
        temp = array[k]
        j = k - 1
        while temp < array[j] and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp


my = []
for x in range(0, 100):
    num = random.randint(1, 101)
    my.append(num)

print(my)
# my=[4,2,35,9,5,6,3]
arraySize = len(my)

insertionSort(my, arraySize)
print(my)