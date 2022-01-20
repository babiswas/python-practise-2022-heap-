from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v,w):
       self.graph[u].append((v,w))
       self.graph[v].append((u,w))

   def dfs_util(self,visited,recstack,u):
       max=0
       visited[u]=True
       recstack[u]=True
       for a,b in self.graph[u]:
           if not visited[a]:
             dist=b+self.dfs_util(visited,recstack,a)
             if dist>max:
                max=dist
           elif recstack[a]==True:
              max=0
              continue
       recstack[u]=False
       return max

   def dfs(self):
       visited=[False]*self.vertex
       recstack=[False]*self.vertex
       for i in range(self.vertex):
          if not visited[i]:
             maxm=self.dfs_util(visited,recstack,i)
       return maxm

if __name__=="__main__":
  graph=Graph(9)
  graph.add_edges(0,1,4)
  graph.add_edges(0,7,8)
  graph.add_edges(1,2,8)
  graph.add_edges(1,7,11)
  graph.add_edges(2,3,7)
  graph.add_edges(2,8,2)
  graph.add_edges(2,5,4)
  graph.add_edges(3,4,9)
  graph.add_edges(3,5,14)
  graph.add_edges(4,5,10)
  graph.add_edges(5,6,2)
  graph.add_edges(6,7,1)
  graph.add_edges(6,8,6)
  graph.add_edges(7,8,7)
  print(graph.dfs())
  