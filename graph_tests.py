import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_add_vertex01(self):
        g = Graph('test1.txt')
        g.add_vertex('1')
        g.add_vertex('2')
        self.assertEqual(g.get_vertices(), ['1', '2', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])
        

    def test_add_edge01(self):
        g = Graph('test1.txt')
        g.add_vertex('v11')
        g.add_vertex('v12')
        g.add_edge('v11','v12')
        self.assertEqual(g.adj_dict['v11'].adjacent_to, ['v12'])
        self.assertEqual(g.adj_dict['v12'].adjacent_to, ['v11'])
        g.add_edge('v11', 'v1')
        self.assertEqual(g.adj_dict['v11'].adjacent_to, ['v12','v1'])
        g.add_edge('v12', 'v3')
        self.assertEqual(g.adj_dict['v12'].adjacent_to, ['v11','v3'])

    def test_get_vertex01(self):
        g = Graph('test2.txt')
        self.assertEqual(g.get_vertex('v5'), None)
        self.assertEqual(g.get_vertex('v1').adjacent_to, ['v2','v3'])
        
    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite()) 

    def test_conn_comp01(self):
        g = Graph('test0.txt')
        self.assertEqual(g.conn_components(), [['v1','v2','v3','v4','v9'],['v10', 'v21', 'v22', 'v5', 'v6', 'v7', 'v8']]) #should this error happen? how do you know when a vertex is in order?
        self.assertFalse(g.is_bipartite())

    def test_add_vertex02(self):
        g = Graph('test5.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3','v4','v5'],['v10','v11','v12','z13'],['v6','v7','v8','v9']])
        self.assertTrue(g.is_bipartite())
    
    def test_06(self):
        g = Graph('test6.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3','v4','v5','v6', 'v7', 'v8','z9']])
        self.assertFalse(g.is_bipartite())


if __name__ == '__main__':
   unittest.main()
