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

        for num in range(6):
            if num != 5:
                self.es.append(graph.Edge(self.vs[num], self.vs[num+1]))
            else:
                self.es.append(graph.Edge(self.vs[num], self.vs[(num+1)%6]))

        self.g = graph.Graph(self.vs,self.es)

    def tearDown(self):
        pass

    def test_get_edge(self):
        '''
        测试1：获取节点0和1的边和[0,1]的边应该相同
        测试2：获取节点3和6不存在边
        '''
        v1 = self.vs[0]
        w1 = self.vs[1]
        e1 = self.g.get_edge(v1, w1)
        if not e1:
            self.fail('test failed')
        self.assertEqual(e1, self.es[0])

        v2 = graph.Vertex('3')
        w2 = graph.Vertex('6')
        e2 = self.g.get_edge(v2, w2)
        if e2:
            self.fail('test failed')

    def test_remove_edge(self):
        """
        测试：删除节点0和节点5的边后再获取节点0和5的边，结果应为：失败
        """
        self.g.remove_edge(self.es[5]);
        v1 = self.vs[0]
        w1 = self.vs[5]
        e1 = self.g.get_edge(v1, w1)
        if e1:
            print "e1 = %s" % str(e1)
            self.fail('test failed')

    def test_vertices(self):
        """
        测试：获取vertices函数返回并比较实际结果，结果应为：成功
        """
        vs = self.g.vertices();
        if sorted(vs) != sorted(self.vs):
            print 'vs = %s' % str(vs)
            print 'self.vs = %s' % str(self.vs)
            self.fail('test failed')

    def test_edges(self):
        """
        测试：获取edge函数返回并比较实际结果，结果应为：成功
        """
        es = self.g.edges()
        if sorted(es) != sorted(self.es):
            print 'es = %s' % str(es)
            print 'self.es = %s' % str(self.es)
            self.fail('test failed')

    def test_out_vertices(self):
        """
        测试：获取节点的相邻节点，并比较实际结果
        """
        v1 = self.vs[3]
        v1_adjacent = self.g.out_vertices(v1)
        if sorted(v1_adjacent) != sorted([self.vs[2],self.vs[4]]):
            print "v1_adjacent = %s" % str(v1_adjacent)
            self.fail('test failed')

    def test_out_edges(self):
        """
        测试：获取节点的边，并比较实际结果
        """
        v1 = self.vs[5]
        e1_adjacent = self.g.out_edges(v1)
        if sorted(e1_adjacent) != sorted([self.es[4],self.es[5]]):
            print "e1_adjacent = %" % str(e1_adjacent)
            self.fail('test failed')

    def test_add_all_edges(self):
        """
        测试：重新建立新的graph，并调用add_all_edges函数，再将g的str形式与实际结果比较
        """
        for i in self.es:
            self.g.remove_edge(i)
        #print '---------------------------------------------------------------------'
        self.g.add_all_edges()
        #print "self.g.edges() = \n%s" % str(self.g.edges())
        #print '---------------------------------------------------------------------'
        
        es = []
        for i in range(5):
            for j in range(i+1,6):
                es.append(graph.Edge(self.vs[i],self.vs[j]))
        #print "es = \n%s" % str(es)
        #print '---------------------------------------------------------------------'
        if (sorted(self.g.vertices()) != sorted(self.vs)) or (sorted(self.g.edges()) != sorted(es)):
            print self.g.vertices()
            print self.g.edges()
            self.fail('test failed')

    def test_add_regular_edges(self):
        """
        测试：节点数为n，度数为m，那么m必须少于n！另外节点数X度数/2=边数，边数必须为整数，因此注意在节点数为奇数时，度数必须为偶数才能够实现正则图。
        测试用例1：
        节点为4，度数为1:结果应为成功
        节点为4，度数为2:结果应为成功
        节点为4，度数为3:结果应为成功
        节点为4，度数为4:结果应为成功
        
        节点数为5，度数为1:结果为失败
        节点数为5，度数为2:结果为成功
        节点数为5，度数为3:结果为失败
        节点数为5，度数为4:结果为成功
        节点数为5，度数为5:结果为失败
        """
        vs1 = [graph.Vertex(i) for i in range(4)]
        result1 = []
        for i in range(1, 5):
            g = graph.Graph(vs1)
            print g
            result1.append(g.add_regular_edge(i))
        if result1 != [true, true, true, true]:
            self.fail('test failed')

        vs2 = [graph.Vertex(i) for i in range(5)]
        result2 = []
        for i in range(1, 6):
            g = graph.Graph(vs2)
            print g
            result2.append(g.add_regular_edge(i))
        if result2 != [false, true, false, true, false]:
            self.fail('test failed')
                
if __name__ == '__main__':
    unittest.main()
