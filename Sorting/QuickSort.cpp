//============================================================================
// Name        : Quick.cpp
// Author      : Sevki Bekir KOCADAG
// Version     : 1.0
// Description : Example of Quick Sort Algorithm in C++
//============================================================================

#include <iostream>
using namespace std;

int partition (int array[], int leftLoc, int rightLoc)
{
	int temp, pivot;
	pivot=array[(leftLoc+rightLoc)/2];
	while(leftLoc<=rightLoc)
	{
		while(array[leftLoc]<pivot)
		{
			leftLoc++;
		}
		while(array[rightLoc]>pivot)
		{
			rightLoc--;
		}
		if(leftLoc<=rightLoc)
		{
			temp=array[leftLoc];
			array[leftLoc]=array[rightLoc];
			array[rightLoc]=temp;
			leftLoc++;
			rightLoc--;
		}
	}

	return leftLoc;
}

void quickSort(int array[], int leftLoc, int rightLoc)
{
	int pivot=partition(array,leftLoc,rightLoc);
	if(leftLoc<pivot-1)
	{
		quickSort(array, leftLoc, pivot-1);
	}
	if(pivot<rightLoc)
	{
		quickSort(array,pivot,rightLoc);
	}
}

int main()
{
	cout << "How many numbers do you sort?"<< endl;
	int size,i;
	cin >> size;
	int arNumber[size];
	cout << "Now, you can write the numbers you want."<< endl;
	for (i=0;i<size;i++)
	{
		cin >> arNumber[i];
	}
	cout << "The numbers are ";
	for (i=0;i<size;i++)
	{
		cout << arNumber[i] << " ";
	}
	cout << endl;
	quickSort(arNumber,0,size-1);
	cout << "The sorted numbers are ";
	for (i=0;i<size;i++)
	{
		cout << arNumber[i] << " ";
	}
	cout << endl;

	return 0;
}
