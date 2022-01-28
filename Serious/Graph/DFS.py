stack = []
visited = [] 
edges = [("A","B"),('A','C'),('B','D'),('B','E'),('C','F'),('E','F')]
class Graph:
    def __init__(self,nodes,is_directed = False):
        self.nodes = nodes 
        self.adj_list = {}
        self.is_directed = is_directed
        for node in self.nodes:
            self.adj_list[node] = []
    def add_edges(self,v,e):
        self.adj_list[v].append(e)
        if not self.is_directed:
            self.adj_list[e].append(v)

        
    def print_adj(self):
        for node in self.nodes:
            print(node+" ",self.adj_list[node])
    def print_degree(self):
        for node in self.nodes:
            print(node+" "+str(len(self.adj_list[node]))+" degree")

    def dfs(self,node):
        if node not in visited:
            print(node,end=" ")
            visited.append(node)
            for neighbour in self.adj_list[node]:
                self.dfs(neighbour)
nodes = ['A','B','C','D','E','F']
graph = Graph(nodes,is_directed=True)
for v,e in edges:
    graph.add_edges(v,e)

graph.dfs("A")

