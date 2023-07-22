// Never finished - abandoned and moved to Python :P

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int find_max(vector<int> v) {
    int max = v.front();
    for (vector<int> :: iterator it = v.begin(); it != v.end(); ++it) {
        if (*it > max) max = *it;
    }
    return max;
}

int main(void) {
    fstream fs("Inputs/Day_01.txt");
    vector<int> cals;
    while (!fs.eof()) {
        int n = 0;
        char s[512];
        fs.getline(s, 2048, '\n');
        while (!fs.fail()) {
            n += stoi(s);
            fs.getline(s, 2048, '\n');
        }
        cout << n << endl;
        cals.push_back(n);
    }
    cout << find_max(cals) << endl;
    return 0;
}
