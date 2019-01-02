#include <iostream>
#include <vector>
#include <set>
using namespace std;

vector<int> readInput(void) {
    vector<int> input;
    int modulation;
    while (cin >> modulation) {
        input.push_back(modulation);
    }
    return input;
}

int main() {
    auto input = readInput();
    
    int frequency = 0;
    set<int> seenFrequencies;
    seenFrequencies.insert(0);

    auto counter = 0;
    while (true) {
        // cout << input.size();
        // cout << counter;
        auto modulation = input[counter];
        frequency += modulation;
        if (seenFrequencies.find(frequency) != seenFrequencies.end()) {
            cout << frequency << endl;
            return 0;
        }
        // for (auto f : seenFrequencies) {
            // cout << f << ",";
        // }
        // cout << endl;
        seenFrequencies.insert(frequency);

        counter = (counter + 1) % input.size();
    }

    cout << frequency;
}