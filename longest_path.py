from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v,w):
       self.graph[u].append((v,w))

   def topsort_util(self,visited,stack,u):
       visited[u]=True
       for a,b in self.graph[u]:
         if not visited[a]:
            self.topsort_util(visited,stack,a)
       stack.append(u)
       

   def topsort(self,src):
       path=[-float("Inf")]*self.vertex
       path[src]=0
       visited=[False]*self.vertex
       stack=list()
       for i in range(self.vertex):
          if not visited[i]:
             self.topsort_util(visited,stack,i)
       while stack:
          u=stack.pop()
          if path[u]!=-float("Inf"):
            for v,w in self.graph[u]:
               if path[v]<path[u]+w:
                  path[v]=path[u]+w
       print(path)

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(0,1,5)
   graph.add_edges(0,2,3)
   graph.add_edges(1,3,6)
   graph.add_edges(1,2,2)
   graph.add_edges(2,4,4)
   graph.add_edges(2,5,2)
   graph.add_edges(2,3,7)
   graph.add_edges(3,5,1)
   graph.add_edges(3,4,-1)
   graph.add_edges(4,5,-2)
   graph.topsort(1)
