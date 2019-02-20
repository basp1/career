from queues import Stack

class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}

    def add(self, child):
        self.children[child.value] = child

class PrefixTree:
    ''' префиксное дерево
    '''
    def __init__(self):
        self.root = Node(None)

    def add(self, lst):
        node = self.root

        for value in lst:
            if not(value in node.children):
                node.children[value] = Node(value)
            node = node.children[value]

    def __iter__(self):
        self.path = Stack()
        self.stack = Stack([self.root])
        self.levels = Stack([0])
        return self

    def __next__(self):
        '''поиск всех путей на префиксном дереве
        '''
        if 0 == self.stack.count:
            raise StopIteration
        else:
            while self.stack.count > 0:
                node = self.stack.pop()
                level = self.levels.pop()
                for i in range(self.path.count - level):
                    self.path.pop()
                self.path.push(node.value)

                if 0 == len(node.children):
                    result = list(self.path)[1:]
                    self.path.pop()
                    return result
                else:
                    for next in node.children.values():
                        self.stack.push(next)
                        self.levels.push(1 + level)

            return result


class DirectedGraph:
    def __init__(self):
        self.adj = {}

    def connect(self, a, b):
        if not (a in self.adj):
            self.adj[a] = []
        self.adj[a] += [b]

    def isConnected(self, a, b):
        ''' проверить существование маршрута между двумя узлами направленного графа
        '''
        stack = Stack([a])
        visited = {a : True}

        while stack.count > 0:
            node = stack.pop()

            if node == b:
                return True

            if not(node in self.adj):
                continue

            for next in self.adj[node]:
                if not(next in visited):
                    stack.push(next)
                    visited[next] = True
        
        return False

    def allPaths(self, a, b):
        '''поиск всех путей между двумя вершинами на направленном циклическом графе
        '''
        paths = PrefixTree()

        path = Stack()
        levels = Stack([0])
        stack = Stack([a])
        visited = {a : True}

        while stack.count > 0:
            node = stack.pop()
            level = levels.pop()
            for i in range(path.count - level):
                prev = path.pop()
                if prev in visited:
                    visited.pop(prev)
            path.push(node)
            visited[node] = True

            if node == b:
                paths.add(list(path))
                visited.pop(b)
            elif node in self.adj:
                for next in self.adj[node]:
                    if not(next in visited):
                        stack.push(next)
                        levels.push(1 + level)
        
        return paths
#
import unittest

class TestGraphs(unittest.TestCase):
    def test_isConnected(self):
        g = DirectedGraph()
        g.connect('a', 'b')
        g.connect('b', 'c')
        g.connect('b', 'd')
        g.connect('d', 'f')
        g.connect('e', 'f')
        g.connect('f', 'g')
        g.connect('g', 'd')

        self.assertTrue(g.isConnected('a', 'b'))
        self.assertTrue(g.isConnected('a', 'c'))
        self.assertTrue(g.isConnected('a', 'd'))
        self.assertTrue(g.isConnected('a', 'f'))
        self.assertTrue(g.isConnected('a', 'g'))
        
        self.assertTrue(g.isConnected('g', 'd'))
        self.assertTrue(g.isConnected('g', 'f'))
        self.assertTrue(g.isConnected('e', 'd'))

        self.assertFalse(g.isConnected('a', 'e'))
        self.assertFalse(g.isConnected('c', 'a'))
        self.assertFalse(g.isConnected('c', 'b'))

        self.assertFalse(g.isConnected('f', 'a'))
        self.assertFalse(g.isConnected('e', 'c'))

    def test_allPaths(self):
        g = DirectedGraph()
        g.connect('a', 'b')
        g.connect('a', 'c')
        g.connect('b', 'd')
        g.connect('c', 'd')

        paths = g.allPaths('a', 'd')
        paths = list(paths)
        self.assertEqual(2, len(paths))
        self.assertEqual(['a','b','d'], paths[0])
        self.assertEqual(['a','c','d'], paths[1])

    def test_allPaths_2(self):
        g = DirectedGraph()
        g.connect('a', 'b')
        g.connect('a', 'c')
        g.connect('b', 'd')
        g.connect('c', 'd')
        g.connect('c', 'e')
        g.connect('e', 'd')

        paths = g.allPaths('a', 'd')
        paths = list(paths)
        self.assertEqual(3, len(paths))
        self.assertEqual(['a','b','d'], paths[0])
        self.assertEqual(['a','c','d'], paths[1])
        self.assertEqual(['a','c','e','d'], paths[2])

    def test_allPaths_3(self):
        g = DirectedGraph()
        g.connect('a', 'b')
        g.connect('b', 'c')
        g.connect('a', 'c')

        paths = g.allPaths('a', 'c')
        paths = list(paths)
        self.assertEqual(2, len(paths))
        self.assertEqual(['a','b','c'], paths[0])
        self.assertEqual(['a','c'], paths[1])

    def test_allPaths_4(self):
        g = DirectedGraph()

        g.connect(0, 3)
        g.connect(3, 0)
        g.connect(3, 6)
        g.connect(6, 3)
        g.connect(0, 4)
        g.connect(4, 0)
        g.connect(4, 7)
        g.connect(7, 4)
        g.connect(4, 5)
        g.connect(5, 4)
        g.connect(5, 7)
        g.connect(7, 5)
        g.connect(0, 2)
        g.connect(2, 0)
        g.connect(0, 1)
        g.connect(1, 0)
        g.connect(1, 2)
        g.connect(2, 1)
        g.connect(1, 5)
        g.connect(5, 1)
        g.connect(2, 5)
        g.connect(5, 2)

        paths = g.allPaths(0, 7)
        paths = list(paths)

        self.assertEqual(10, len(paths))

    def test_allPaths_5(self):
        g = DirectedGraph()

        g.connect(0, 1)
        g.connect(1, 0)
        g.connect(0, 2)
        g.connect(2, 0)
        g.connect(2, 3)
        g.connect(3, 2)
        g.connect(3, 4)
        g.connect(4, 3)
        g.connect(2, 5)
        g.connect(5, 2)
        g.connect(1, 5)
        g.connect(5, 1)
        g.connect(5, 4)
        g.connect(4, 5)
        g.connect(3, 6)
        g.connect(6, 3)
        g.connect(4, 6)
        g.connect(6, 4)

        paths = g.allPaths(1, 5)
        paths = list(paths)

        self.assertEqual(4, len(paths))

    def test_allPaths_6(self):
        g = DirectedGraph()

        g.connect(0, 1)
        g.connect(1, 0)
        g.connect(0, 2)
        g.connect(2, 0)
        g.connect(2, 3)
        g.connect(3, 2)
        g.connect(3, 4)
        g.connect(4, 3)
        g.connect(2, 5)
        g.connect(5, 2)
        g.connect(1, 5)
        g.connect(5, 1)
        g.connect(5, 4)
        g.connect(4, 5)
        g.connect(3, 6)
        g.connect(6, 3)
        g.connect(4, 6)
        g.connect(6, 4)

        paths = g.allPaths(0, 6)
        paths = list(paths)

        self.assertEqual(8, len(paths))
            
    def test_allPaths_7(self):
        g = DirectedGraph()

        g.connect(0, 1)
        g.connect(1, 0)
        g.connect(1, 2)
        g.connect(2, 1)
        g.connect(1, 3)
        g.connect(3, 1)
        g.connect(3, 4)
        g.connect(4, 3)
        g.connect(3, 6)
        g.connect(6, 3)
        g.connect(4, 8)
        g.connect(8, 4)
        g.connect(8, 5)
        g.connect(5, 8)
        g.connect(6, 7)
        g.connect(7, 6)
        g.connect(7, 5)
        g.connect(5, 7)
        g.connect(7, 3)
        g.connect(3, 7)

        paths = g.allPaths(0, 2)
        paths = list(paths)

        self.assertEqual(1, len(paths))

    def test_allPaths_8(self):
        g = DirectedGraph()

        g.connect(0, 1)
        g.connect(1, 0)
        g.connect(0, 2)
        g.connect(2, 0)
        g.connect(0, 3)
        g.connect(3, 0)
        g.connect(0, 4)
        g.connect(4, 0)
        g.connect(1, 2)
        g.connect(2, 1)
        g.connect(1, 3)
        g.connect(3, 1)
        g.connect(1, 4)
        g.connect(4, 1)
        g.connect(2, 3)
        g.connect(3, 2)
        g.connect(2, 4)
        g.connect(4, 2)
        g.connect(3, 4)
        g.connect(4, 3)

        paths = g.allPaths(0, 4)
        paths = list(paths)

        self.assertEqual(16, len(paths))

    def test_allPaths_9(self):
        g = DirectedGraph()

        g.connect(0, 1)
        g.connect(1, 0)
        g.connect(0, 2)
        g.connect(2, 0)
        g.connect(0, 3)
        g.connect(3, 0)
        g.connect(0, 4)
        g.connect(4, 0)
        g.connect(1, 2)
        g.connect(2, 1)
        g.connect(1, 3)
        g.connect(3, 1)
        g.connect(1, 4)
        g.connect(4, 1)
        g.connect(2, 3)
        g.connect(3, 2)
        g.connect(2, 4)
        g.connect(4, 2)
        g.connect(3, 4)
        g.connect(4, 3)

        paths = g.allPaths(0, 4)
        paths = list(paths)

        self.assertEqual(16, len(paths))


if __name__ == '__main__':
    unittest.main()