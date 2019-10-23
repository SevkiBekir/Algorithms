
def hourglassSum(arr):
    sums=[]
    for i in range(0,4):
        temp = arr[i:i+3]
        for j in range(0,4):
            tempSum = temp[0][j] + temp[0][j+1] + temp[0][j+2] + temp[1][j+1] + temp[2][j] + temp[2][j+1] + temp[2][j+2]
            sums.append(tempSum)
    #         print("temp:")
    #         print(temp)
    # print(sums)
    return max(sums)



if __name__ == "__main__":
    arr = []
    #temp = "-9 -9 -9  1 1 1 0 -9  0  4 3 2 -9 -9 -9  1 2 3 0  0  8  6 6 0 0  0  0 -2 0 0 0  0  1  2 4 0"
    temp = "1 1 1 0 0 0 0 1 0 0 0 0 1 1 1 0 0 0 0 0 2 4 4 0 0 0 0 2 0 0 0 0 1 2 4 0"
    # print(map(temp.rstrip().split()))
    arr = list(map(int,temp.rstrip().split()))
    # print(len(arr))
    tempList=[]
    # print(arr)
    for i in range(6):
        tempList.append(arr[i*6:i*6+6])

    print(tempList[0:3])
    # temp = "1 1 1 0 0 0"
    # tempList.append(list(map(int,temp.rstrip().split())))
    # temp = "0 1 0 0 0 0"
    # tempList.append(list(map(int,temp.rstrip().split())))
    # temp = "1 1 1 0 0 0"
    # tempList.append(list(map(int,temp.rstrip().split())))
    # temp = "0 0 0 0 0 0"
    # tempList.append(list(map(int,temp.rstrip().split())))
    # temp = "0 0 0 0 0 0"
    # tempList.append(list(map(int,temp.rstrip().split())))
    # temp = "0 0 0 0 1 1"
    # tempList.append(list(map(int,temp.rstrip().split())))

    print(tempList)
    denem = tempList[3:6]
    print(len(denem))
    print(hourglassSum(tempList))