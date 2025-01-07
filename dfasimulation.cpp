#include <iostream>
#include <string>
using namespace std;

// Define states
enum State { START, S0, S1 };

State transition(State currentState, char input) 
{
    switch (currentState) 
    {
        case START:
            return (input == '0') ? S0 : START;
        case S0:
            return (input == '1') ? S1 : START;
        case S1:
            return (input == '0') ? S0 : START;
        default:
            return START;
    }
}

bool accepts(const string& input) 
{
    State currentState = START;
    for (char c : input) {
        currentState = transition(currentState, c);
    }
    return currentState == S1; // Accept if final state is S1
}

int main() 
{
    string input;
    cout << "Enter a binary string: ";
    cin >> input;

    if (accepts(input)) {
        cout << "The string is accepted by the DFA.\n";
    } else {
        cout << "The string is rejected by the DFA.\n";
    }

    return 0;
}
