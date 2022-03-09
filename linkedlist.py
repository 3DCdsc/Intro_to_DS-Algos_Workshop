class Node:

    """
    A node contains its own data, as well as a "next" attribute that
    points to another node
    """
    def __init__(self, data):
        # Write code here

    """Returns Data of the current node"""
    def getData(self):
        return self.data

    """Returns the node that this node points to"""
    def getNext(self):
        return self.next

    """Gives the current node data"""
    def setData(self, newdata):
        self.data = newdata

    """set the current's node next node"""
    def setNext(self, next):
        self.next = next


class LinkedList:
    """Head is the FIRST node in the Linked List"""
    def __init__(self):
        # Write code here

    """Turns the item into a Node, set its next node to the current head, then make it the new head
    Always add to the front of the LinkedList. Scandalous"""
    def add(self, item):
        # Write code here

    """Iteratively searches nodes' data until we get the one we're looking for, then remove it"""
    def remove(self, item):
        # Write code here

    """Checks if the linked list is empty"""
    def isEmpty(self):
        return self.head == None

    """Counts every single node, and return the count value"""
    def size(self):
        # Write code here

    """Recursively searches for the node that we want, containing the data we're looking for
    Once found, we return a boolean"""
    def search(self, item):
        # Write code here

# Write test code here

