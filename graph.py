class Graph(dict):
    def __init__(self, vs=[], es=[]):
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        self[v] = {}

    def add_edge(self, e):
        v,w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v, w):
        try:
            if self[v][w] == self[w][v]:
                return self[v][w]
        except KeyError:
            return None

class Vertex(object):
    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        return "Vertex(%(label)s)" % {'label':repr(self.label)}

    __str__ = __repr__

class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1, e2))

    def __repr__(self):
        return "Edge(%(e1)s,%(e2)s)" % {'e1':repr(self[0]), 'e2':repr(self[1])}

    __str__ = __repr__

def main():
    v = Vertex('v')
    w = Vertex('w')
    e = Edge(v, w)
    print v, w, e

    g = Graph([v, w], [e])
    print g

if __name__ == '__main__':
    main()

