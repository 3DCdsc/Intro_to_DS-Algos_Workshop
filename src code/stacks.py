# This is a stack class
class Stack:
    # Stacks store items in a list
    def __init__(self):
        self.items = []

    # Pop removes last item of the stack
    def pop(self):
        return self.items.pop()

    # Push adds an item to the back of the stack
    def push(self, item):
        return self.items.append(item)

    # Peek returns the last item of the stack WITHOUT removing it
    def peek(self):
        return self.items[len(self.items) - 1]

    # isEmpty checks if the stack is Empty
    def isEmpty(self):
        return self.items == []

    # Size returns the number of items in the stack
    def size(self):
        return len(self.items)


# Test Code
myStack = Stack()
print(f"Is my stack Empty? {myStack.isEmpty()}")

# Add items to stack
myStack.push(1)
myStack.push(2)

# Show last item in stack
print(f"{myStack.peek()}")

# Remove last item in stack
myStack.pop()
print(f"{myStack.peek()}")


