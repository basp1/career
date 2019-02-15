#!/usr/bin/python
from copy import copy
from sys import maxsize

from linked import *

class MinStack:
    ''' стек, в котором кроме push и рор будет поддерживаться функция min, возвращающая минимальный элемент
    все методы push, рор и min должны выполняться за время O(1)
    '''
    def __init__(self):
        self.values = []
        self.n = 0
        self.mins = []

    def push(self, value):
        if self.n == len(self.values):
            self.values += [0]
            self.mins += [maxsize]
        
        self.values[self.n] = value
        self.mins[self.n] = min(value, self.mins[self.n - 1])
        self.n += 1

    def pop(self):
        assert self.n > 0

        self.n -= 1

        return self.values[self.n]

    def min(self):
        assert self.n > 0

        return self.mins[self.n - 1]

#
import unittest

class TestQueues(unittest.TestCase):

    def test_minstack(self):
        ms = MinStack()
        
        ms.push(5)
        self.assertEqual(5, ms.min())

        ms.push(5)
        self.assertEqual(5, ms.min())

        ms.push(6)
        self.assertEqual(5, ms.min())

        ms.push(4)
        self.assertEqual(4, ms.min())

        ms.push(3)
        self.assertEqual(3, ms.min())

        ms.push(2)
        self.assertEqual(2, ms.min())

        ms.push(1)
        self.assertEqual(1, ms.min())

        ms.pop()
        self.assertEqual(2, ms.min())

        ms.pop()
        self.assertEqual(3, ms.min())

        ms.pop()
        self.assertEqual(4, ms.min())

        ms.pop()
        self.assertEqual(5, ms.min())

        ms.pop()
        self.assertEqual(5, ms.min())

        ms.pop()
        self.assertEqual(5, ms.min())

if __name__ == '__main__':
    unittest.main()
