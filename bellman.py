class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=[]

   def add_edges(self,u,v,w):
      self.graph.append((u,v,w))

   def display(self,src,path):
      for i in range(self.vertex):
        print(f"({src},{i},{path[i]})")

   def bellman_ford(self,src):
       path=[float("Inf") for i in range(self.vertex)]
       path[src]=0
       for i in range(self.vertex-1):
         for u,v,w in self.graph:
            if path[u]!=float("Inf") and path[u]+w<path[v]:
               path[v]=path[u]+w
       for u,v,w in self.graph:
           if path[u]+w<path[v]:
              print("There is a negative cycle in the graph")
       self.display(0,path)


if __name__=="__main__":
   graph=Graph(5)
   graph.add_edges(0,1,-1)
   graph.add_edges(0,2,4)
   graph.add_edges(1,2,3)
   graph.add_edges(1,3,2)
   graph.add_edges(1,4,2)
   graph.add_edges(3,2,5)
   graph.add_edges(3,1,1)
   graph.add_edges(4,3,-3)
   graph.bellman_ford(0)
