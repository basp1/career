#!/usr/bin/python
from copy import copy
from stringbuf import Stringbuf
import math

def isunique(string):
    '''определить, есть ли в строке повторяющиеся символы
    '''

    # if len(string) > 256:
    #    return False

    set = {}

    for ch in string:
        if ch in set:
            return False
        else:
            set[ch] = True

    return True


def ispermutable(string1, string2):
    '''является ли первая строка перестановкой символов второй строки
    '''

    if len(string1) != len(string2):
        return False

    n = len(string1)
    chars = {}

    for ch in string1:
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 1

    for ch in string2:
        if ch in chars:
            chars[ch] -= 1
        else:
            return False

    for v in chars.values():
        if 0 != v:
            return False

    return True


def ispalindromable(string):
    '''является ли строка палиндромом после перестановки
    '''

    string = string.lower()
    n = len(string)
    odds = {}

    for ch in string:
        if ' ' == ch:
            n -= 1
            continue
        if ch in odds:
            odds[ch] = not odds[ch]
        else:
            odds[ch] = True

    oddcount = 0
    oddlen = n % 2
    for odd in odds.values():
        if odd:
            oddcount += 1
        if 0 == oddlen and oddcount > 0:
            return False
        elif 1 == oddlen and oddcount > 1:
            return False

    return True


def ismodifiable(string1, string2):
    '''находятся ли две строки на расстоянии одной модификации (или нуля модификаций)
    допустимы три вида модификаций: вставка символа, удаление символа и замена символа
    '''

    n1 = len(string1)
    n2 = len(string2)

    if abs(n1 - n2) > 1:
        return False

    diff = False
    i1 = i2 = 0
    while i1 < n1 and i2 < n2:
        if string1[i1] != string2[i2]:
            if diff:
                return False
            diff = True

            if i2 < n2 - 1 and string1[i1] == string2[i2 + 1]:
                i2 += 1
            if i1 < n1 - 1 and string1[i1 + 1] == string2[i2]:
                i1 += 1

        i1 += 1
        i2 += 1

    return True


def replacespace(string, n):
    '''заменить все пробелы в строке символами '%20'
    длина строки позволяет сохранить дополнительные символы
    фактическая длина строки известна заранее
    '''

    old = ' '
    new = '%20'

    lst = list(string)
    m = len(new)

    olds = 0
    for i in range(n):
        if old == lst[i]:
            olds += 1
    olds *= m - 1

    if 0 == olds:
        return string

    i = n - 1
    j = n + olds - 1

    while j >= 0:
        if old != lst[i]:
            lst[j] = lst[i]
        else:
            for k in range(m):
                lst[j - k] = new[-(k + 1)]
            j -= m - 1
        i -= 1
        j -= 1

    string = ''.join(lst)
    return string


def rotate90(matrix):
    ''' поворот матрицы NxN на 90 градусов
    '''
    assert len(matrix) == len(matrix[0])

    n = len(matrix)

    for i in range(int(n / 2)):
        for j in range(i, n - i - 1):
            t = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = t

    return matrix


def compress(string):
    '''сжимать строку с использова­нием счетчика повторяющихся символов
    например, строка aabcccccaaa пре­вращается в a2b1c5a3
    если сжатая строка не становится короче исходной, то возвращать исходную строку
    предполагается, что строка состоит только из букв верхнего и нижнего регистра (a-z)
    '''
    
    def countdigits(x):
        return int(1 + math.log10(x))

    def checklen(string):
        n = len(string)
        m = 0
        j = 1
        prev = string[0]
        for ch in string[1:n]:
            if ch == prev:
                j += 1
            else:
                m += 1
                if j > 0:
                    m += countdigits(j)
                    j = 1
            prev = ch
        m += 1 + countdigits(j)
        return m

    n = len(string)
    if n < 3:
        return string

    m = checklen(string)
    if m >= n:
        return string

    out = Stringbuf(m)
    
    j = 1
    prev = string[0]
    for ch in string[1:n]:
        if ch == prev:
            j += 1
        else:
            out.append(prev)
            if j > 0:
                out.append(str(j))
                j = 1

        prev = ch

    out.append(prev)
    if j > 0:
        out.append(str(j))
    
    return str(out)

#
import unittest


class TestArrays(unittest.TestCase):

    def test_isunique(self):
        self.assertTrue(isunique(''))
        self.assertTrue(isunique('a'))
        self.assertTrue(isunique('a_'))
        self.assertTrue(isunique('aA'))
        self.assertTrue(isunique('abc'))
        self.assertTrue(isunique('qwertyuiopasdfghjklzxcvbnm'))
        self.assertTrue(isunique('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

        self.assertFalse(isunique('aa'))
        self.assertFalse(isunique('AA'))
        self.assertFalse(isunique('AaA'))
        self.assertFalse(isunique('1a1'))
        self.assertFalse(isunique('aba'))
        self.assertFalse(isunique('baa'))
        self.assertFalse(isunique('qwertyuiopasdfghjklzxcvbnmqa'))

    def test_ispermutable(self):
        self.assertTrue(ispermutable('', ''))
        self.assertFalse(ispermutable('', 'a'))
        self.assertFalse(ispermutable('a', ''))

        self.assertTrue(ispermutable('aaa', 'aaa'))
        self.assertTrue(ispermutable('aba', 'baa'))
        self.assertTrue(ispermutable('abc', 'cab'))

        self.assertFalse(ispermutable('aa', 'ba'))
        self.assertFalse(ispermutable('abc', 'abca'))
        self.assertFalse(ispermutable('abcd', 'abca'))
        self.assertFalse(ispermutable('abc', 'dab'))
        self.assertFalse(ispermutable('abc', 'abd'))

    def test_ispalindrome(self):
        self.assertTrue(ispalindromable(''))
        self.assertTrue(ispalindromable('a'))
        self.assertTrue(ispalindromable('aa'))
        self.assertTrue(ispalindromable('aaa'))
        self.assertTrue(ispalindromable('aba'))
        self.assertTrue(ispalindromable('abba'))
        self.assertTrue(ispalindromable('abab'))
        self.assertTrue(ispalindromable('abbba'))
        self.assertTrue(ispalindromable('abcba'))
        self.assertTrue(ispalindromable('abcacba'))
        self.assertTrue(ispalindromable('TactCoa'))
        self.assertTrue(ispalindromable('Tact Coa'))

        self.assertFalse(ispalindromable('ab'))
        self.assertFalse(ispalindromable('ba'))
        self.assertFalse(ispalindromable('abc'))
        self.assertFalse(ispalindromable('ababbe'))
        self.assertFalse(ispalindromable('abcbbcaa'))

    def test_ismodifiable(self):
        self.assertTrue(ismodifiable('', ''))
        self.assertTrue(ismodifiable('pale', 'pale'))
        self.assertTrue(ismodifiable('pale', 'pakle'))
        self.assertTrue(ismodifiable('pales', 'pale'))
        self.assertTrue(ismodifiable('pale', 'pales'))
        self.assertTrue(ismodifiable('pale', 'bale'))
        self.assertTrue(ismodifiable('bale', 'pale'))
        self.assertTrue(ismodifiable('pale', 'ple'))
        self.assertTrue(ismodifiable('ple', 'pale'))
        self.assertTrue(ismodifiable('pale', 'spale'))
        self.assertTrue(ismodifiable('', 'p'))
        self.assertTrue(ismodifiable('p', ''))

        self.assertFalse(ismodifiable('pale', 'bake'))
        self.assertFalse(ismodifiable('pale', 'paky'))
        self.assertFalse(ismodifiable('pale', 'palesy'))
        self.assertFalse(ismodifiable('', 'pale'))
        self.assertFalse(ismodifiable('pale', ''))
        self.assertFalse(ismodifiable('pale', 'spaly'))

    def test_replacespace(self):
        self.assertEqual(replacespace('Mr John Smith    ', 13), 'Mr%20John%20Smith')
        pass

    def test_rotate90(self):
        m = [[1,2,3],
             [4,5,6],
             [7,8,9]]
        
        e = [[7,4,1],
             [8,5,2],
             [9,6,3]]
        
        self.assertNotEqual(e, m)
        rotate90(m)
        self.assertEqual(e, m)

        m = [[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12],
             [13,14,15,16]]
        
        e = [[13,9,5,1],
             [14,10,6,2],
             [15,11,7,3],
             [16,12,8,4]]

        self.assertNotEqual(e, m)
        rotate90(m)
        self.assertEqual(e, m)

        m = [[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11,12,13,14,15],
             [16,17,18,19,20],
             [21,22,23,24,25]]

        e = [[21,16,11,6,1],
             [22,17,12,7,2],
             [23,18,13,8,3],
             [24,19,14,9,4],
             [25,20,15,10,5]]

        self.assertNotEqual(e, m)
        rotate90(m)
        self.assertEqual(e, m)
    
    def test_compress(self):
        self.assertEqual('', compress(''))
        self.assertEqual('ab', compress('ab'))
        self.assertEqual('abcdef', compress('abcdef'))
        self.assertEqual('ababab', compress('ababab'))
        self.assertEqual('aa', compress('aa'))
        self.assertEqual('aabb', compress('aabb'))
        self.assertEqual('abb', compress('abb'))
        self.assertEqual('abcc', compress('abcc'))
        self.assertEqual('abbb', compress('abbb'))
        self.assertEqual('aaab', compress('aaab'))
        self.assertEqual('abccc', compress('abccc'))

        self.assertEqual('a3', compress('aaa'))
        self.assertEqual('a1b4', compress('abbbb'))
        self.assertEqual('a3b2', compress('aaabb'))
        self.assertEqual('a1b2c5', compress('abbccccc'))
        self.assertEqual('a1b1c5', compress('abccccc'))
        self.assertEqual('a10', compress('aaaaaaaaaa'))
        self.assertEqual('a2b1c5a3', compress('aabcccccaaa'))

if __name__ == '__main__':
    unittest.main()
