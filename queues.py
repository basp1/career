#!/usr/bin/python
from copy import copy
from sys import maxsize

from linked import *

class Stack:
    def __init__(self, values = []):
        self.count  = 0
        self.values = []
        for value in values:
            self.push(value)

    def push(self, value):
        if self.count == len(self.values):
            self.values += [0]
            
        self.values[self.count] = value
        self.count += 1

    def pop(self):
        assert self.count > 0
        
        self.count -= 1

        return self.values[self.count]

    def top(self):
        return self.values[self.count - 1]

    def __iter__(self):
        self.cur = 0
        return self
    def __next__(self):
        if self.cur >= self.count:
            raise StopIteration
        else:
            result = self.values[self.cur]
            self.cur += 1
            return result


class MinStack:
    ''' стек, в котором кроме push и рор будет поддерживаться функция min, возвращающая минимальный элемент
    все методы push, рор и min должны выполняться за время O(1)
    '''
    def __init__(self):
        self.values = Stack()
        self.mins = Stack()

    def push(self, value):       
        self.values.push(value)
        
        if 0 == self.mins.count:
            self.mins.push(value)
        else:
            self.mins.push(min(value, self.min()))

    def pop(self):
        self.mins.pop()
        
        return self.values.pop()

    def min(self):
        return self.mins.top()


class SortedStack:
    ''' стек, в котором элементы хранятся и извлекаются в отсортированном порядке
    разрешается использовать другой стек для временного хранилища данных
    '''
    def __init__(self):
        self.stack = Stack()

    def push(self, value):
        if 0 == self.stack.count:
            self.stack.push(value)
        else:
            ss = Stack()

            while self.stack.count > 0 and value > self.stack.top():
                t = self.stack.pop()
                ss.push(t)

            self.stack.push(value)

            while ss.count > 0:
                t = ss.pop()
                self.stack.push(t)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack.top()

class Queue2:
    ''' очередь с использованием двух стеков
    '''
    def __init__(self):
        self.stack = Stack()
        self.pops = Stack()
        self.count = 0

    def enqueue(self, value):
        self.stack.push(value)
        self.count += 1

    def dequeue(self):
        assert self.count > 0

        if 0 == self.pops.count:
            while self.stack.count > 0:
                t = self.stack.pop()
                self.pops.push(t)

        self.count -= 1

        return self.pops.pop()

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

    def test_sortedstack(self):
        ss = SortedStack()

        ss.push(4)
        self.assertEqual([4], ss.stack.values)

        ss.push(4)
        self.assertEqual([4,4], ss.stack.values)
        
        ss.push(2)
        self.assertEqual([4,4,2], ss.stack.values)

        ss.push(3)
        self.assertEqual([4,4,3,2], ss.stack.values)

        ss.push(10)
        self.assertEqual([10,4,4,3,2], ss.stack.values)

        ss.push(1)
        self.assertEqual([10,4,4,3,2,1], ss.stack.values)

    def test_queue2(self):
        qq = Queue2()

        qq.enqueue(1)
        qq.enqueue(2)
        qq.enqueue(3)

        self.assertEqual(3, qq.count)

        self.assertEqual(1, qq.dequeue())        
        self.assertEqual(2, qq.count)

        self.assertEqual(2, qq.dequeue())
        self.assertEqual(1, qq.count)

        self.assertEqual(3, qq.dequeue())
        self.assertEqual(0, qq.count)

        qq.enqueue(1)
        qq.enqueue(2)
        qq.enqueue(3)
        self.assertEqual(3, qq.count)

        self.assertEqual(1, qq.dequeue())
        self.assertEqual(2, qq.count)

        qq.enqueue(4)
        self.assertEqual(3, qq.count)
        self.assertEqual(2, qq.dequeue())
        self.assertEqual(2, qq.count)
        
        qq.enqueue(5)
        self.assertEqual(3, qq.count)
        self.assertEqual(3, qq.dequeue())
        self.assertEqual(2, qq.count)
        
        self.assertEqual(4, qq.dequeue())
        self.assertEqual(1, qq.count)

        self.assertEqual(5, qq.dequeue())
        self.assertEqual(0, qq.count)        

if __name__ == '__main__':
    unittest.main()
