
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None        

class Linked:
    def __init__(self, lst):
        self.head = Node()
        
        node = self.head
        prev = None
        for item in lst:
            node.value = item            
            if None != prev:
                prev.next = node
            prev = node
            node = Node()

    def append(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

