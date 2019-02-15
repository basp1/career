
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None        

class Linked:
    def __init__(self, lst):
        if 0 == len(lst):
            self.head = None
            return

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

    def reverse(self):
        if None == self.head or None == self.head.next:
            return self
    
        k = 0
        p = self.head
        n = p.next
        p.next = None
        while None != p:
            if None == n:
                self.head = p
                break
            t = n.next
            n.next = p
            p = n
            n = t
        
        return self

    def __len__(self):        
        k = 0

        p = self.head
        while None != p:
            k += 1
            p = p.next

        return k

    def __iter__(self):
        self.cur = self.head
        return self
    def __next__(self):
        if None == self.cur:
            raise StopIteration
        else:
            result = self.cur.value
            self.cur = self.cur.next
            return result

#
import unittest

class TestLinked(unittest.TestCase):

    def test_list(self):
        self.assertEqual([], list(Linked([])))
        self.assertEqual([1], list(Linked([1])))
        self.assertEqual([1,2], list(Linked([1,2])))
        self.assertEqual([1,2,3], list(Linked([1,2,3])))
        self.assertEqual([1,2,3,4], list(Linked([1,2,3,4])))

    def test_append(self):
        lst = Linked([])
        lst.append(3)
        lst.append(2)
        lst.append(1)

        self.assertEqual([1,2,3], list(lst))

    def test_append_2(self):
        lst = Linked([3,4])
        lst.append(2)
        lst.append(1)

        self.assertEqual([1,2,3,4], list(lst))

    def test_reverse(self):        
        lst = Linked([])
        self.assertEqual([], list(lst.reverse()))

        lst = Linked([1])
        self.assertEqual([1], list(lst.reverse()))

        lst = Linked([1,2])
        self.assertEqual([2,1], list(lst.reverse()))

        lst = Linked([1,2,3])
        self.assertEqual([3,2,1], list(lst.reverse()))

        lst = Linked([1,2,3,4])
        self.assertEqual([4,3,2,1], list(lst.reverse()))

        lst = Linked([1,2,3,4,5])
        self.assertEqual([5,4,3,2,1], list(lst.reverse()))

if __name__ == '__main__':
    unittest.main()
