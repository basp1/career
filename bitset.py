from copy import copy
from array import array
from math import ceil

class Bitset:
    def __init__(self, bitCount):
        assert bitCount > 0

        n = ceil(bitCount / 32)
        self.values = array('L', [0] * n)
        self.bitCount = bitCount

    def __getitem__(self, index):
        assert index < self.bitCount
        
        i = index >> 5
        x = self.values[i]
        x >>= (index % 32)
        x &= 1

        if 1 == x:
            return True
        else:
            return False

    def __setitem__(self, index, value):
        assert index < self.bitCount

        i = index >> 5
        x = 1 << (index % 32)
        if value:
            self.values[i] |= x
        else:
            x = ~x
            self.values[i] &= x
        

#
import unittest


class TestBitset(unittest.TestCase):

    def test_set(self):
        b = Bitset(10)
        self.assertEqual(1, len(b.values))

        b[1] = True
        self.assertEqual(2, b.values[0])

        b[0] = True
        self.assertEqual(3, b.values[0])

        b[7] = True
        self.assertEqual(131, b.values[0])

        b[0] = False
        self.assertEqual(130, b.values[0])

        b[1] = False
        self.assertEqual(128, b.values[0])

        b[7] = False
        self.assertEqual(0, b.values[0])

    def test_set_2(self):
        b = Bitset(1)
        self.assertEqual(1, len(b.values))

        b = Bitset(32)
        self.assertEqual(1, len(b.values))

        b = Bitset(33)
        self.assertEqual(2, len(b.values))

        b = Bitset(63)
        self.assertEqual(2, len(b.values))

        b = Bitset(64)
        self.assertEqual(2, len(b.values))

        b = Bitset(65)
        self.assertEqual(3, len(b.values))

    def test_set_3(self):
        b = Bitset(100)
        self.assertEqual(4, len(b.values))

        for i in range(8):
            b[i] = True        
        self.assertEqual(255, b.values[0])

        for i in range(8, 16):
            b[i] = True
        self.assertEqual(65535, b.values[0])

        for i in range(8):
            b[i] = False
        self.assertEqual(65280, b.values[0])

        for i in range(8, 16):
            b[i] = False
        self.assertEqual(0, b.values[0])

        b[16] = True
        self.assertEqual(65536, b.values[0])
        
        b[33] = True
        self.assertEqual(2, b.values[1])
 
    def test_get(self):
        b = Bitset(100)
        self.assertEqual(4, len(b.values))

        b[3] = True
        self.assertFalse(b[0])
        self.assertFalse(b[1])
        self.assertFalse(b[2])
        self.assertTrue(b[3])
        self.assertFalse(b[4])
        self.assertFalse(b[5])

        b[50] = True
        self.assertFalse(b[0])
        self.assertFalse(b[18])
        self.assertTrue(b[50])
        self.assertFalse(b[72])

if __name__ == '__main__':
    unittest.main()
