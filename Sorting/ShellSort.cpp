//============================================================================
// Name        : Shell.cpp
// Author      : Sevki Bekir KOCADAG
// Version     : 1.0
// Description : Example of Shell Sort Algorithm in C++
//============================================================================

#include <iostream>
using namespace std;

void insertionSort(int array[],int select,int k)
{
	int i,j,temp,size;
	size=sizeof(array);
	for (i = 1; i <= size-1; i++)
	{

		for (j=i;j>0 && array[j]<array[j-1];j--)
		{
			temp=array[j];
			array[j]=array[j-1];
			array[j-1]=temp;

		}
	}
}

int main() {
	cout << "How many numbers do you sort?"<< endl;
	int size,i,j,h=1;
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
	while(h<size)
	{
		h=3*h+1;

	}
	while(h>0)
	{
		h/=3;
		for(j=1;j<h;j++)
		{
			insertionSort(arNumber,h,j);
		}
	}


	return 0;
}
