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
#
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

if __name__ == '__main__':
    unittest.main()
