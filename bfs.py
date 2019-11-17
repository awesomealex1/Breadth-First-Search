from graph import Graph
from vertex import Vertex
from math import inf

def create_graph():
	g = Graph()
	A = Vertex("A")
	g.add_v(A)
	B = Vertex("B")
	g.add_v(B)
	C = Vertex("C")
	g.add_v(C)
	D = Vertex("D")
	g.add_v(D)
	E = Vertex("E")
	g.add_v(E)
	F = Vertex("F")
	g.add_v(F)
	g.add_e(A,B)
	g.add_e(A,C)
	g.add_e(B,C)
	g.add_e(B,D)
	g.add_e(B,F)
	g.add_e(D,E)
	g.add_e(D,F)
	g.add_e(E,F)
	return g,A

g,A = create_graph()

def BFS(g,s):
	for v in g.vertices:
		v.color = "white"
		v.d = inf
		v.pre = None
	s.color = "gray"
	s.d = 0
	s.pre = None
	q = []
	q.append(s)
	while q != []:
		v = q.pop()
		for u in g.adjacents(v):
			if u.color == "white":
				u.color = "gray"
				u.d = v.d + 1
				u.pre = v
				q.append(u)
		v.color = "black"
	for v in g.vertices:
		print(v.name,v.d)

BFS(g,A)