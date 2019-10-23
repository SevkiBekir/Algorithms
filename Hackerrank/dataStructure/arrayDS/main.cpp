#include <iostream>
#include <vector>

using namespace std;

void arraySolution(){
    int arrayCounter = 0;
    int *array;
    cin >> arrayCounter;
    array = new int[arrayCounter];
    for (int i = 0; i < arrayCounter; ++i) {
        cin >> array[i];
    }

    for (int j = arrayCounter-1; j >= 0; j--) {
        cout << array[j] << " ";
    }
}

vector<int> reverseArray(vector<int> a) {
    vector<int> reverse;
    for(vector<int>::iterator it = a.end() - 1; it != a.begin()-1; --it){
        reverse.push_back(*it);
    }

    return reverse;

}


int main() {
    int arrayCounter = 0;
    cin >> arrayCounter;
    vector<int> v;
    for (int i = 0; i < arrayCounter; ++i) {
        int temp;
        cin >> temp;
        v.push_back(temp);
    }

    for (int i = 0; i < v.size(); i++) {
        cout << v[i];

        if (i != v.size() - 1) {
            cout << " ";
        }
    }

    vector<int> reverse = reverseArray(v);
    for (int i = 0; i < reverse.size(); i++) {
        cout << reverse[i];

        if (i != reverse.size() - 1) {
            cout << " ";
        }
    }


    //arraySolution();
    return 0;
}