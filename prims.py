import sys
class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=None

   def get_index(self,index,visited):
       minm=sys.maxsize
       my_index=0
       for i in range(len(index)):
          if not visited[i]:
             if minm>index[i]:
                minm=index[i]
                my_index=i
       return my_index
                 

   def prims_algo(self,src):
       index=[sys.maxsize]*self.vertex
       visited=[False]*self.vertex
       parent=[None for i in range(self.vertex)]
       parent[src]=-1
       index[src]=0
       for i in range(self.vertex-1):
          new_index=self.get_index(index,visited)
          visited[new_index]=True
          for j in range(self.vertex):
             if self.graph[new_index][j]!=0 and visited[j]==False and self.graph[new_index][j]<index[j]:
                index[j]=self.graph[new_index][j]
                parent[j]=new_index
       print(parent)
       for index in range(self.vertex):
           print(f"{parent[index]},{index},{self.graph[index][parent[index]]}")
       

if __name__=="__main__":
   graph=Graph(5)
   graph.graph=[[0,2,0,6,0],[2,0,3,8,5],[0,3,0,0,7],[6,8,0,0,9],[0,5,7,9,0]]
   graph.prims_algo(0)
   
        
      