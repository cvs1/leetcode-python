class MinStack:
    def __init__(self):
        # Initialize the stack and the min_stack as empty lists
        self.stack = []  # Main stack to store the values
        self.min_stack = []  # Auxiliary stack to store the minimums

    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.stack.append(val)
        # If the min_stack is empty or the current value is smaller or equal to the current minimum, push it onto the min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop the top value from the main stack
        if self.stack:
            popped_val = self.stack.pop()
            # If the popped value is the same as the current minimum, pop it from the min_stack too
            if popped_val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        # Return the current minimum element from the min_stack
        if self.min_stack:
            return self.min_stack[-1]

# Create an instance of MinStack
minStack = MinStack()

# Push some values to the stack
minStack.push(-2)
minStack.push(0)
minStack.push(-3)

# Debugging: Check the current minimum after pushing elements
print("Current minimum:", minStack.getMin())  # Expected: -3

# Pop an element and check the top and minimum values
minStack.pop()
print("Top element after pop:", minStack.top())  # Expected: 0
print("Current minimum after pop:", minStack.getMin())  # Expected: -2

# Push more values and check the minimum
minStack.push(1)
minStack.push(-1)
print("Current minimum after pushing 1 and -1:", minStack.getMin())  # Expected: -2
