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

if __name__ == '__main__':
    unittest.main()
