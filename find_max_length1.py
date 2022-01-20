from collections import defaultdict
class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v,w):
       self.graph[u].append((v,w))
       self.graph[v].append((u,w))

   def find_max(self):
       maxm=-1
       visited=[False]*self.vertex
       for i in range(self.vertex):
         if not visited[i]:
            dist=self.find_max_length(visited,i)
            if dist>maxm:
               maxm=dist
       return maxm

   def find_max_length(self,visited,u):
       maxm=0
       visited[u]=True
       for a,b in self.graph[u]:
          if not visited[a]:
             dist=b+self.find_max_length(visited,a)
             if maxm<dist:
                maxm=dist
       return maxm

if __name__=="__main__":
   graph=Graph(7)
   graph.add_edges(1,2,3)
   graph.add_edges(2,3,4)
   graph.add_edges(2,6,2)
   graph.add_edges(6,4,6)
   graph.add_edges(6,5,5)
   print(graph.find_max())
   print("Constructing another graph")
   graph1=Graph(6)
   graph1.add_edges(0,1,2)
   graph1.add_edges(1,2,6)
   graph1.add_edges(0,3,5)
   graph1.add_edges(0,4,4)
   graph1.add_edges(4,5,9)
   print(graph1.find_max())
    
   
       
   
   