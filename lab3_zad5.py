class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}
        self.output = None

    def add_transition(self, input_symbol, next_state, output=None):
        self.transitions[input_symbol] = (next_state, output)

    def next_state(self, input_symbol):
        if input_symbol in self.transitions:
            return self.transitions[input_symbol]
        else:
            raise ValueError(f"No transition defined for input '{input_symbol}' in state '{self.name}'.")


class MealyMachine:
    def __init__(self):
        self.states = {}
        self.initial_state = None

    def add_state(self, state):
        self.states[state.name] = state

    def set_initial_state(self, state_name):
        self.initial_state = self.states[state_name]

    def process(self, inputs):
        current_state = self.initial_state
        outputs = []

        for input_symbol in inputs:
            if current_state is None:
                raise ValueError("Initial state is not set.")
            next_state, output = current_state.next_state(input_symbol)
            outputs.append(output)
            current_state = next_state

        return outputs


class MooreMachine:
    def __init__(self):
        self.states = {}
        self.initial_state = None

    def add_state(self, state):
        self.states[state.name] = state

    def set_initial_state(self, state_name):
        self.initial_state = self.states[state_name]

    def process(self, inputs):
        current_state = self.initial_state
        outputs = []

        for input_symbol in inputs:
            if current_state is None:
                raise ValueError("Initial state is not set.")
            outputs.append(current_state.output)
            next_state, _ = current_state.next_state(input_symbol)
            current_state = next_state

        outputs.append(current_state.output)
        return outputs


if __name__ == "__main__":
    # Mealy
    state_A = State("A")
    state_B = State("B")
    state_C = State("C")

    state_A.add_transition("0", state_A, "0")
    state_A.add_transition("1", state_B, "1")
    state_B.add_transition("0", state_C, "0")
    state_B.add_transition("1", state_A, "1")
    state_C.add_transition("0", state_B, "1")
    state_C.add_transition("1", state_C, "0")

    mealy = MealyMachine()
    mealy.add_state(state_A)
    mealy.add_state(state_B)
    mealy.add_state(state_C)
    mealy.set_initial_state("A")

    inputs = "10101"
    print("Mealy Machine Outputs:", mealy.process(inputs))

    # Moore
    state_X = State("X")
    state_Y = State("Y")
    state_Z = State("Z")

    state_X.output = "0"
    state_Y.output = "1"
    state_Z.output = "0"

    state_X.add_transition("0", state_X)
    state_X.add_transition("1", state_Y)
    state_Y.add_transition("0", state_Z)
    state_Y.add_transition("1", state_X)
    state_Z.add_transition("0", state_Y)
    state_Z.add_transition("1", state_Z)

    moore = MooreMachine()
    moore.add_state(state_X)
    moore.add_state(state_Y)
    moore.add_state(state_Z)
    moore.set_initial_state("X")

    print("Moore Machine Outputs:", moore.process(inputs))
