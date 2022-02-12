class Node:

    """
    A node contains its own data, as well as a "next" attribute that
    points to another node
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    # Returns Data of the current node
    def getData(self):
        return self.data

    # Returns the node that this node points to
    def getNext(self):
        return self.next

    # Gives the current node data
    def setData(self, newdata):
        self.data = newdata

    # set the current's node next node
    def setNext(self, next):
        self.next = next


class LinkedList:
    # Head is the FIRST node in the Linked List
    def __init__(self):
        self.head = None

    # Turns the item into a Node, set its next node to the current head, then make it the new head
    # Always add to the front of the LinkedList
    # Scandalous
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    # Iteratively searches nodes' data until we get the one we're looking for, then remove it
    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    # Checks if the linked list is empty
    def isEmpty(self):
        return self.head == None

    # Counts every single node, and return the count value
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    # Recursively searches for the node that we want, containing the data we're looking for
    # Once found, we return a boolean
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found


myList = LinkedList()
myList.add(1)
myList.add(2)

# Check if values are in the list
print(f"{myList.search(1)}")
print(f"{myList.search(2)}")

# Remove and check
myList.remove(2)
print(f"{myList.search(2)}")

