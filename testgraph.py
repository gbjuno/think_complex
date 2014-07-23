# -*- coding: utf-8 -*-
import graph
import unittest

class TestGraph(unittest.TestCase):
    """
    初始化构造一个简单图进行验证分析
    图如下所见：
    (0)--(1)--(2)--(3)--(4)--(5)--(0)
    """
    def setUp(self):
        self.vs = []; self.es = [];
        for num in range(6):
            self.vs.append(graph.Vertex('%s' % num))
        print self.vs

        for num in range(6):
            if num != 5:
                self.es.append(graph.Edge(self.vs[num], self.vs[num+1]))
            else:
                self.es.append(graph.Edge(self.vs[num], self.vs[(num+1)%6]))
        print self.es

        self.g = graph.Graph(self.vs,self.es)
        print self.g

    def tearDown(self):
        pass

    def test_get_edge(self):
        v1 = self.vs[0]
        w1 = self.vs[1]
        e1 = self.g.get_edge(v1, w1)
        if not e1:
            self.fail('test failed')
        else:
            print '---------------------'
            print e1
            print '---------------------'
        self.assertEqual(e1, self.es[0])
        if e1 == graph.Edge(v1, w1):
            print "e1 is equal to Edge(v1,w1)"

        v2 = graph.Vertex('3')
        w2 = graph.Vertex('6')
        e2 = self.g.get_edge(v2, w2)
        if not e2:
            self.fail('test failed')
        else:
            print e2

if __name__ == '__main__':
    unittest.main()
