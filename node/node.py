class Node():
    def __init__(self, state, parent = None, action = None, neighboards = None) -> None:
        self.state = state
        self.parent = parent
        self.action = action
        self.neighboards = neighboards  
