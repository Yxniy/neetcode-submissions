class MinStack:

    def __init__(self):
        self.stack = []
        # Second stack to track the minimums
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # If min_stack is empty OR val is smaller than current min, push val
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            # OPTIONAL: Some people duplicate the top min here to keep lengths equal.
            # But it saves space to ONLY push if it's a new minimum.
            # Note: For the logic below, we are only pushing if it's a NEW min or EQUAL.
            pass

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop() # Actually removes the item
            # If the item we just popped was the minimum, pop it from min_stack too
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1] # Instant access!