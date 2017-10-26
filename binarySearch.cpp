//
// Created by sbk on 26.10.2017.
//
#include <iostream>

int binarySearch(int *arr, int key, int lower, int higher);

int main() {
    std::cout << "Hello, World!" << std::endl;

    int* myArray = new int[20];


    for(int i = 0;i<20;i++){
        if(i >= 17)
            myArray[i] = i-16;
        else
            myArray[i] = i+4;
        std::cout<< myArray[i]<< "-";
    }
    std::cout<<std::endl;
    int size = sizeof(myArray);

    int result = binarySearch(myArray,5,0,19);

    std::cout<< result<<std::endl;


    return 0;
}

int binarySearch(int *arr, int key, int lower, int higher){
    int mid = (lower+higher)/2;


    // key not present
    if(lower > higher)
        return -1;
    // key found
    if(arr[mid] == key )
        return mid;
    // if left half is sorted.
    if(arr[lower] <= arr[mid]){
        // if key is present in left half.
        if(arr[lower] <= key && arr[mid] >= key)
            return binarySearch(arr,key,lower,mid-1);
        // if key is not present in left hald..search right half.
        else
            return binarySearch(arr,key,mid+1,higher);
    }
    // if left half is sorted.
    else{
        // if key is present in right half.
        if(arr[mid]<= key && arr[higher]>= key)
            return binarySearch(arr,key,mid+1,higher);
        // if key is not present in right half..search in left half.
        else
            return binarySearch(arr,key,lower,mid-1);

    }


}

