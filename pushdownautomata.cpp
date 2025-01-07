#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool isBalanced(const string& input) 
{
    stack<char> pdaStack;

    for (char c : input) 
    {
        if (c == '(') {
            pdaStack.push(c); // Push '(' onto the stack
        } else if (c == ')') {
            if (pdaStack.empty() || pdaStack.top() != '(') 
            {
                return false; // Unmatched ')'
            }
            pdaStack.pop(); // Match found, pop the stack
        }
    }

    return pdaStack.empty(); // Check if stack is empty at the end
}

int main() 
{
    string input;
    cout << "Enter a string of parentheses: ";
    cin >> input;

    if (isBalanced(input)) {
        cout << "The string has balanced parentheses.\n";
    } else {
        cout << "The string does not have balanced parentheses.\n";
    }

    return 0;
}
