from queues import Stack

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