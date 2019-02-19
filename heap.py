#!/usr/bin/python
import math

class Heap:
    def __init__(self, func, capacity=0):
        self.values = [None] * capacity
        self.func = func
        self.count = 0

    def append(self, value):
        index = self.count
        if len(self.values) <= index:
            self.values += [None]
        self.values[index] = value
        self.count += 1
        self.__promote(index)

    def __promote(self, index):
        assert index >= 0 and index < self.count

        if 0 == index:
            return

        parent = int(index / 2)
        while index > 0:
            t = self.values[index]
            if t != self.func(t, self.values[parent]):
                break
            self.values[index] = self.values[parent]
            self.values[parent] = t
            next = parent
            parent = int(index / 2)
            index = next
            

    def remove(self):
        assert self.count > 0

        last = self.values[self.count - 1]
        self.values[0] = last
        self.count -= 1
        self.__demote(0)

    def __demote(self, index):
        assert index >= 0 and index < self.count

        if self.count == (1 + index):
            return
        value = self.values[index]

        while index < self.count:
            right = (1 + index) * 2
            left = right - 1
            rv = lv = None
            if right < self.count:
                rv = self.values[right]
            if left < self.count:
                lv = self.values[left]
            
            child = -1
            if None != lv and None != rv and lv == self.func(lv, rv):
                child = left
            elif None != rv:
                child = right
            elif None != lv:
                child = left

            if child < 0 or value == self.func(value, self.values[child]):
                break
            else:
                self.values[index] = self.values[child]
                self.values[child] = value
                index = child


    def top(self):
        assert self.count > 0

        return self.values[0]

    def height(self):
        return 1 + int(math.log2(self.count))


#
import unittest

class TestHeap(unittest.TestCase):
    def test_append(self):
        h = Heap(lambda x,y: min(x,y))
        
        h.append(3)
        self.assertEqual(3, h.top())
        self.assertEqual(1, h.height())

        h.append(4)
        self.assertEqual(3, h.top())
        self.assertEqual(2, h.height())

        h.append(5)
        self.assertEqual(3, h.top())
        self.assertEqual(2, h.height())

        h.append(2)
        self.assertEqual(2, h.top())
        self.assertEqual(3, h.height())

        h.append(1)
        self.assertEqual(1, h.top())
        self.assertEqual(3, h.height())

    def test_append2(self):
        h = Heap(lambda x,y: min(x,y))
        
        for i in range(8, -1, -1):
            h.append(i)

        self.assertEqual(0, h.top())
        self.assertEqual(4, h.height())

        h.append(9)
        self.assertEqual(0, h.top())
        self.assertEqual(4, h.height())
       
    
    def test_capacity(self):
        h = Heap(lambda x,y: min(x,y), 5)
        for i in range(8, -1, -1):
            h.append(i)

        self.assertEqual(0, h.top())
        self.assertEqual(4, h.height())

        h.append(9)
        self.assertEqual(0, h.top())
        self.assertEqual(4, h.height())

    def test_remove(self):
        h = Heap(lambda x,y: min(x,y))
        h.append(18)
        h.append(19)
        h.append(20)        
        self.assertEqual(18, h.top())

        h.remove()
        self.assertEqual(19, h.top())

        h.remove()
        self.assertEqual(20, h.top())

    def test_remove2(self):
        h = Heap(lambda x,y: min(x,y))
        for i in range(8, -1, -1):
            h.append(i)
        
        self.assertEqual(0, h.top())
        self.assertEqual(4, h.height())

        h.remove()
        self.assertEqual(1, h.top())
        self.assertEqual(4, h.height())

        h.remove()
        self.assertEqual(2, h.top())
        self.assertEqual(3, h.height())

        h.remove()
        self.assertEqual(3, h.top())
        self.assertEqual(3, h.height())

        h.remove()
        self.assertEqual(4, h.top())
        self.assertEqual(3, h.height())

    def test_remove3(self):
        n = 20
        h = Heap(lambda x,y: min(x,y))
        for i in range(n, 0, -1):
            h.append(i)
        
        self.assertEqual(1, h.top())

        for i in range(0, int(n / 2)):
            h.remove()
        self.assertEqual(1 + n / 2, h.top())

        for i in range(0, int((n / 2) - 1)):
            h.remove()
        self.assertEqual(n, h.top())



if __name__ == '__main__':
    unittest.main()