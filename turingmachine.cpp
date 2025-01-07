#include <iostream>
#include <vector>
using namespace std;

void incrementBinary(vector<char>& tape) 
{
    int i = tape.size() - 1;
    while (i >= 0 && tape[i] == '1') {
        tape[i] = '0';
        i--;
    }
    if (i >= 0) {
        tape[i] = '1';
    } else {
        tape.insert(tape.begin(), '1'); // Carry overflow
    }
}

int main() 
{
    string input;
    cout << "Please enter a binary number: ";
    cin >> input;

    vector<char> tape(input.begin(), input.end());
    incrementBinary(tape);

    cout << "Next binary number: ";
    for (char c : tape) 
    {
        cout << c;
    }
    cout << endl;
    return 0;
}
