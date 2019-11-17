from vertex import Vertex

class Graph:

	def __init__(self):
		self.vertices = []
		self.adj = {}

	def add_v(self,v):
		self.vertices.append(v)

	def add_e(self,u,v):

		if u.name in self.adj:
			self.adj[u.name].append(v)
		else:
			self.adj[u.name] = [v]

		if v.name in self.adj:
			self.adj[v.name].append(u)
		else:
			self.adj[v.name] = [u]

	def adjacents(self,v):
		return self.adj[v.name]