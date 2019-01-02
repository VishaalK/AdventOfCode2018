#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;

vector<string> readInput(void) {
    string str;
    vector<string> ret;
    while (getline(cin, str)) {
        ret.push_back(str);
    }
    return ret;
}

map<char, int> countLine(const string& line) {
    map<char, int> ret;
    for (char c : line) {
        ret[c]++;
    }
    return ret;
}

bool numberOfDifferingCharacters(const string& a, const string& b) {
    int numberOfDifferingCharacters = 0;
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) {
            numberOfDifferingCharacters++;
        }

        if (numberOfDifferingCharacters > 1) {
            return false;
        }
    }

    return numberOfDifferingCharacters == 1;
}

string getCommonCharacters(const string& l, const string& r) {
    string ret;
    for (int i = 0; i < l.size(); i++) {
        if (l[i] == r[i]) {
            ret += l[i];
        }
    }

    return ret;
}

int main() {
    auto input = readInput();

    for (int i = 0; i < input.size(); i++) {
        for (int j = i + 1; j < input.size(); j++) {
            bool differsByTwo = numberOfDifferingCharacters(input[i], input[j]);
            if (differsByTwo) {
                cout << getCommonCharacters(input[i], input[j]) << endl;
                return 0;
            }
        }
    }

    return -1;
}

// int main() {
//     string str;

//     int numTwos = 0;
//     int numThrees = 0;

//     while (getline(cin, str)) {
//         auto counts = countLine(str);
//         set<int> countsAsSet;
//         for (auto kv : counts) {
//             countsAsSet.insert(kv.second);
//         }

//         if (countsAsSet.find(2) != countsAsSet.end()) {
//             numTwos++;
//         }

//         if (countsAsSet.find(3) != countsAsSet.end()) {
//             numThrees++;
//         }
//     }

//     cout << numTwos << "," << numThrees << endl;
//     cout << numTwos * numThrees << endl;
//     return 0;
// }
