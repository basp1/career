class Stringbuf:
    def __init__(self, capacity=1):
        assert(capacity > 0)

        self.chars = [' '] * capacity
        self.index = 0

    def capacity(self):
        return len(self.chars)

    def append(self, items):
        self.expand(self.index + len(items))
        for ch in items:
            self.chars[self.index] = ch
            self.index += 1

    def expand(self, capacity):
        oldcap = self.capacity()

        if oldcap >= capacity:
            return
        else:            
            newcap = oldcap
            while newcap < capacity:
                newcap *= 2
            self.chars += [' '] * (newcap - oldcap)

    def __str__(self):
        return ''.join(self.chars[0 : self.index])

#
import unittest


class TestStringbuf(unittest.TestCase):

    def test_init(self):
        s = Stringbuf()
        self.assertEqual(1, s.capacity())

        s = Stringbuf(1)
        self.assertEqual(1, s.capacity())

        s = Stringbuf(10)
        self.assertEqual(10, s.capacity())

    def test_append(self):
        s = Stringbuf()

        s.append('a')
        self.assertEqual(1, s.capacity())

        s.append('b')
        self.assertEqual(2, s.capacity())

        s.append('c')
        self.assertEqual(4, s.capacity())

        s.append('d')
        self.assertEqual(4, s.capacity())

        s.append('e')
        self.assertEqual(8, s.capacity())

        s.append('f')
        self.assertEqual(8, s.capacity())
        
    def test_append_2(self):
        s = Stringbuf()

        s.append('abc')
        self.assertEqual(4, s.capacity())

        s.append('def')
        self.assertEqual(8, s.capacity())
        
    def test_append_3(self):
        s = Stringbuf(6)
        self.assertEqual(6, s.capacity())

        s.append('abcdef')
        self.assertEqual(6, s.capacity())

        s.append('a')
        self.assertEqual(12, s.capacity())

    def test_string(self):
        s = Stringbuf()

        s.append('abcdef')
        self.assertEqual(8, s.capacity())

        self.assertEqual('abcdef', str(s))

    def test_string_2(self):
        s = Stringbuf()

        s.append('a')
        s.append('bc')
        s.append('def')
        self.assertEqual('abcdef', str(s))

if __name__ == '__main__':
    unittest.main()
