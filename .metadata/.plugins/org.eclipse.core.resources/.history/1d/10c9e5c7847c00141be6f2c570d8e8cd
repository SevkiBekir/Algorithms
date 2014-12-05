//============================================================================
// Name        : Insertion.cpp
// Author      : Sevki Bekir Kocadag
// Version     :
// Copyright   : All rights reserved.
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main()
{
	cout << "How many number do you sort?"<< endl;
	int size,i,j,temp;
	cin >> size;
	int arNumber[size];
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
	for (i = 1; i <= size-1; i++)
	{

		for (j=i;j>0 && arNumber[j]<arNumber[j-1];j--)
		{
			temp=arNumber[j];
			arNumber[j]=arNumber[j-1];
			arNumber[j-1]=temp;

		}
	}
	cout << "The sorted numbers are ";
	for (i=0;i<size;i++)
	{
		cout << arNumber[i] << " ";
	}
	cout << endl;
	return 0;
}
