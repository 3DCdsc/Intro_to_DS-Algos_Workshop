class Queue:

    # Queue stores data in a list
    def __init__(self):
        self.items = []

    # Enqueue inserts a new item at the front of the list
    def enqueue(self, item):
        self.items.insert(0, item)

    # Dequeue removes items at the back of the list (first item that came in)
    def dequeue(self):
        self.items.pop()

    # Size returns the number of items in the queue
    def size(self):
        return len(self.items)

    # isEmpty checks if the queue is empty, returns a boolean
    def isEmpty(self):
        return self.items == []


# Testing it out
myQueue = Queue()

# Add items to the queue
myQueue.enqueue(1)
myQueue.enqueue(2)
print(f"{myQueue.items}")

# Remove an item (First in gets removed)
myQueue.dequeue()
print(f"{myQueue.items}")

