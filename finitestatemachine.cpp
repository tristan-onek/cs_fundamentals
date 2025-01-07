#include <iostream>
#include <string>
using namespace std;

// Define states
enum State { START, Q1, Q2, ACCEPT, REJECT };

State transition(State currentState, char input) {
    switch (currentState) {
        case START:
            return (input == 'a') ? Q1 : REJECT;
        case Q1:
            return (input == 'b') ? Q2 : REJECT;
        case Q2:
            return (input == 'a') ? ACCEPT : REJECT;
        case ACCEPT:
            return (input == 'b') ? Q2 : REJECT;
        default:
            return REJECT;
    }
}

bool isAccepted(const string& input) 
{
    State currentState = START;
    for (char c : input) {
        currentState = transition(currentState, c);
        if (currentState == REJECT) 
        {
            return false;
        }
    }
    return currentState == ACCEPT;
}

int main() 
{
    string input;
    cout << "Enter a string (e.g., 'aba', 'ababa'): ";
    cin >> input;

    if (isAccepted(input)) 
    {
        cout << "String is accepted by the automaton.\n";
    } else {
        cout << "String is rejected by the automaton.\n";
    }

    return 0;
}
