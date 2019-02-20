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
        stack = Stack()
        stack.push(a)
        visited = {a : True}
        while stack.count > 0:
            vertex = stack.pop()

            if vertex == b:
                return True

            if not(vertex in self.adj):
                continue

            for next in self.adj[vertex]:
                if not(next in visited):
                    stack.push(next)
                    visited[next] = True
        
        return False

    
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


if __name__ == '__main__':
    unittest.main()