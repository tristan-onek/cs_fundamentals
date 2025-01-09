# Deterministic finite automaton demo in Python

class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        """
        Initialize the Deterministic finite automaton.
        :param states: Set of states in the Deterministic finite automaton.
        :param alphabet: Set of input symbols.
        :param transitions: Dictionary with keys as (state, symbol) and values as next state.
        :param start_state: Initial state of DFA.
        :param accept_states: Set of accepting states.
        """
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, input_string):
        """
        Check if the DFA accepts the given input string.
        :param input_string: String to process.
        :return: True if accepted, False otherwise.
        """
        current_state = self.start_state
        for symbol in input_string:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
            else:
                return False  # Transition not defined
        return current_state in self.accept_states


# Example usage:
if __name__ == "__main__":
    # Define the DFA
    states = {"q0", "q1", "q2"}
    alphabet = {"0", "1"}
    transitions = {
        ("q0", "0"): "q1",
        ("q0", "1"): "q0",
        ("q1", "0"): "q2",
        ("q1", "1"): "q0",
        ("q2", "0"): "q2",
        ("q2", "1"): "q2",
    }
    start_state = "q0"
    accept_states = {"q2"}

    # Create a DFA instance
    dfa = DFA(states, alphabet, transitions, start_state, accept_states)

    # Test strings
    test_strings = ["0", "00", "000", "001", "111"]
    for test_string in test_strings:
        result = dfa.accepts(test_string)
        print(f"Input: {test_string} -> Accepted: {result}")
