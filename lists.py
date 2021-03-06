#!/usr/bin/python
from copy import copy

from linked import *

def getrevitem(lst, k):
    '''найти в односвязном списке k-ый с конца элемент
    '''
    assert k >= 0

    k -= 1
    p1 = lst.head
    p2 = p1.next
    while k >= 0 and None != p2:
        p2 = p2.next
        k -= 1

    if k >= 0:
        return None

    while None != p2:
        p1 = p1.next
        p2 = p2.next

    if None == p1:
        return None
    else:
        return p1.value

def removedup(lst):
    ''' удаление дубликатов из несортированного связного списка
    '''
    if None == lst.head:
        return lst

    p1 = lst.head
    while None != p1:
        prev = p1
        p2 = p1.next
        while None != p2:
            if p1.value == p2.value:
                prev.next = p2.next
                p2 = p2.next
            else:
                prev = p2
                p2 = p2.next
        p1 = p1.next
    return lst


def removedup2(lst):
    ''' удаление дубликатов из несортированного связного списка
    '''
    if None == lst.head:
        return lst

    set = {}
    p = lst.head
    prev = None
    while None != p:
        if p.value in set:
            prev.next = p.next
            p = p.next
        else:
            set[p.value] = True
            prev = p
            p = p.next
    return lst

def removenode(node):
    '''удалить элемент из середины связного списка
    доступ предоставляется только к этому узлу
    '''
    assert None != node and None != node.next

    next = node.next
    node.value = next.value
    node.next = next.next

    
def ispalindrome(lst):
    '''является ли связный список палиндромом
    '''
    n = len(lst)

    if n < 2:
        return True
    
    i = 0
    p = lst.head
    stack = []
    while i < int(n / 2):
        stack += [p.value]
        p = p.next
        i += 1

    if 1 == (n % 2):
        i += 1
        p = p.next

    j = len(stack) - 1
    while i < n:
        if stack[j] != p.value:
            return False
        p = p.next        
        j -= 1
        i += 1

    return True

def sumlists(lst1, lst2):
    ''' суммировать два числа, представленных в виде связных списков
    каждый узел такого списка пред­ставляет один разряд, все цифры хранятся в обратном порядке
    результат возвращать также в виде связного списка
    '''
    p1 = lst1.head
    p2 = lst2.head
    
    m = 0
    res = []
    while None != p1 or None != p2:
        s = m
        if None != p1:
            s += p1.value
        if None != p2:
            s += p2.value

        if s >= 10:
            res += [s - 10]
            m = 1
        else:
            res += [s]
            m = 0

        if None != p1:
            p1 = p1.next
        if None != p2:
            p2 = p2.next

    if m > 0:
        res += [1]

    return Linked(res)

def findcycle(lst):
    if None == lst.head or None == lst.head.next:
        return None

    p1 = lst.head
    p2 = lst.head.next

    while None != p1 and None != p2 and p1 != p2:
        if None != p1.next:
            p1 = p1.next
        if None != p2.next:
            p2 = p2.next
        
        if None == p2.next:
            return None
        else:
            p2 = p2.next

    if p1 == p2:
        return p1
    else:
        return None

#
import unittest

class TestLists(unittest.TestCase):

    def test_getrevitem(self):
        lst = Linked([1,2,3,4,5,6,7])
        
        x = getrevitem(lst, 0)
        self.assertEqual(7, x)

        x = getrevitem(lst, 1)
        self.assertEqual(6, x)

        x = getrevitem(lst, 2)
        self.assertEqual(5, x)

        x = getrevitem(lst, 3)
        self.assertEqual(4, x)

        x = getrevitem(lst, 4)
        self.assertEqual(3, x)

        x = getrevitem(lst, 5)
        self.assertEqual(2, x)

        x = getrevitem(lst, 6)
        self.assertEqual(1, x)

        x = getrevitem(lst, 7)
        self.assertEqual(None, x)
        
        x = getrevitem(lst, 8)
        self.assertEqual(None, x)

    def test_removedup(self):
        lst = removedup(Linked([]))
        self.assertEqual([], list(lst))

        lst = removedup(Linked([1]))
        self.assertEqual([1], list(lst))

        lst = removedup(Linked([1,2,3]))
        self.assertEqual([1,2,3], list(lst))

        lst = removedup(Linked([1,1]))
        self.assertEqual([1], list(lst))

        lst = removedup(Linked([1,1,1]))
        self.assertEqual([1], list(lst))

        lst = removedup(Linked([1,2,1]))
        self.assertEqual([1,2], list(lst))

        lst = removedup(Linked([1,2,2]))
        self.assertEqual([1,2], list(lst))

        lst = removedup(Linked([1,2,1,2]))
        self.assertEqual([1,2], list(lst))

        lst = removedup(Linked([1,2,1,2,1,2,1,2]))
        self.assertEqual([1,2], list(lst))

        lst = removedup(Linked([1,1,1,1,1,1,1,2,2,2,2]))
        self.assertEqual([1,2], list(lst))

    def test_removedup2(self):
        lst = removedup2(Linked([]))
        self.assertEqual([], list(lst))

        lst = removedup2(Linked([1]))
        self.assertEqual([1], list(lst))

        lst = removedup2(Linked([1,2,3]))
        self.assertEqual([1,2,3], list(lst))

        lst = removedup2(Linked([1,1]))
        self.assertEqual([1], list(lst))

        lst = removedup2(Linked([1,1,1]))
        self.assertEqual([1], list(lst))

        lst = removedup2(Linked([1,2,1]))
        self.assertEqual([1,2], list(lst))

        lst = removedup2(Linked([1,2,2]))
        self.assertEqual([1,2], list(lst))

        lst = removedup2(Linked([1,2,1,2]))
        self.assertEqual([1,2], list(lst))

        lst = removedup2(Linked([1,2,1,2,1,2,1,2]))
        self.assertEqual([1,2], list(lst))

        lst = removedup2(Linked([1,1,1,1,1,1,1,2,2,2,2]))
        self.assertEqual([1,2], list(lst))

    def test_removenode(self):
        lst = Linked([1,2,3,4,5])
        
        node2 = lst.head.next
        removenode(node2)
        self.assertEqual([1,3,4,5], list(lst))

        node3 = lst.head.next
        removenode(node3)
        self.assertEqual([1,4,5], list(lst))

        node4 = lst.head.next
        removenode(node4)
        self.assertEqual([1,5], list(lst))

    def test_ispalindrome(self):
        self.assertTrue(ispalindrome(Linked([])))
        self.assertTrue(ispalindrome(Linked([1])))
        self.assertTrue(ispalindrome(Linked([1,1])))
        self.assertTrue(ispalindrome(Linked([1,1,1])))
        self.assertTrue(ispalindrome(Linked([1,2,1])))
        self.assertTrue(ispalindrome(Linked([1,2,2,1])))
        self.assertTrue(ispalindrome(Linked([1,2,1,2,1])))
        self.assertTrue(ispalindrome(Linked([1,2,3,2,1])))
        self.assertTrue(ispalindrome(Linked([1,2,3,3,2,1])))
        self.assertTrue(ispalindrome(Linked([1,2,4,3,4,2,1])))

        self.assertFalse(ispalindrome(Linked([1,2])))
        self.assertFalse(ispalindrome(Linked([1,2,3])))
        self.assertFalse(ispalindrome(Linked([1,2,3,1])))
        self.assertFalse(ispalindrome(Linked([1,2,2,3])))
        self.assertFalse(ispalindrome(Linked([1,2,3,2,3])))
        self.assertFalse(ispalindrome(Linked([1,2,3,4,5])))
        self.assertFalse(ispalindrome(Linked([1,2,3,3,3,1])))
        self.assertFalse(ispalindrome(Linked([1,2,3,3,3,3,1])))

    def test_sumlists(self):
        lst = sumlists(Linked([0]), Linked([0]))
        self.assertEqual([0], list(lst))

        lst = sumlists(Linked([3]), Linked([3]))
        self.assertEqual([6], list(lst))

        lst = sumlists(Linked([5]), Linked([5]))
        self.assertEqual([0,1], list(lst))

        lst = sumlists(Linked([5]), Linked([7]))
        self.assertEqual([2,1], list(lst))

        lst = sumlists(Linked([1,1,1]), Linked([9]))
        self.assertEqual([0,2,1], list(lst))

        lst = sumlists(Linked([0,0,1]), Linked([0,0,2]))
        self.assertEqual([0,0,3], list(lst))

        lst = sumlists(Linked([7,1,6]), Linked([5,9,2]))
        self.assertEqual([2,1,9], list(lst))

        lst = sumlists(Linked([2,4,5]), Linked([4,0,2]))
        self.assertEqual([6,4,7], list(lst))

        lst = sumlists(Linked([9,9,9]), Linked([9,9,9]))
        self.assertEqual([8,9,9,1], list(lst))

        lst = sumlists(Linked([5,2]), Linked([1,0,0,1]))
        self.assertEqual([6,2,0,1], list(lst))

        lst = sumlists(Linked([2]), Linked([9,9,9,9]))
        self.assertEqual([1,0,0,0,1], list(lst))

    def test_findcycle(self):
        ''' найти для кольцевого связного списка начальный узел петли
        '''
        lst = Linked(['a', 'b', 'c', 'd', 'e'])
        c = lst.head.next.next
        e = c.next.next
        
        self.assertEqual('c', c.value)
        self.assertEqual(None, e.next)

        e.next = c
        self.assertEqual(c, findcycle(lst))

        self.assertEqual(None, findcycle(Linked([])))
        self.assertEqual(None, findcycle(Linked(['a'])))
        self.assertEqual(None, findcycle(Linked(['a', 'b'])))
        self.assertEqual(None, findcycle(Linked(['a', 'b', 'c'])))
        self.assertEqual(None, findcycle(Linked(['a', 'b', 'c', 'd'])))
        self.assertEqual(None, findcycle(Linked(['a', 'b', 'c', 'd', 'e'])))

        lst = Linked(['a'])
        a = lst.head
        a.next = a
        
        self.assertEqual(a, findcycle(lst))


if __name__ == '__main__':
    unittest.main()
