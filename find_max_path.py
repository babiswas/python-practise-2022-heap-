from collections import defaultdict
class Graph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.graph=defaultdict(list)

    def add_edges(self,u,v,w):
        self.graph[u].append((v,w))
        self.graph[v].append((u,w))

    def find_longest_util(self,visited,u,mylist,wt):
        visited[u]=True
        for a,b in self.graph[u]:
           if not visited[a]:
              self.find_longest_util(visited,a,mylist,wt+b)
        mylist.append((u,wt))
               
               
    def find_longest(self):
        mylist=[]
        visited=[False]*self.vertex
        for i in range(self.vertex):
           if not visited[i]:
              self.find_longest_util(visited,i,mylist,0)
        return mylist

if __name__=="__main__":
   graph=Graph(7)
   graph.add_edges(1,2,3)
   graph.add_edges(2,3,4)
   graph.add_edges(2,6,2)
   graph.add_edges(6,4,6)
   graph.add_edges(6,5,5)
   print(graph.find_longest()) 
   graph1=Graph(6)
   graph1.add_edges(0,1,2)
   graph1.add_edges(1,2,6)
   graph1.add_edges(0,3,5)
   graph1.add_edges(0,4,4)
   graph1.add_edges(4,5,9)
   print(graph1.find_longest())