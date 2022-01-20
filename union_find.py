class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=[]

   def add_edges(self,u,v):
      self.graph.append((u,v))

   def find(self,u,arr):
      if arr[u]!=-1:
        return self.find(arr[u],arr)
      return u
 
   def union(self,u,v,arr):
       index1=self.find(u,arr)
       index2=self.find(v,arr)
       if index1!=index2:
          arr[index1]=index2
       elif index1==index2:
           return

   def makeset(self):
       arr=[-1 for i in range(self.vertex)]
       for u,v in self.graph:
          index1=self.find(u,arr)
          index2=self.find(v,arr)
          if index1!=index2:
             self.union(index1,index2,arr)
          else:
             return True
       return False

if __name__=="__main__":
   graph=Graph(9)
   graph.add_edges(4,0)
   graph.add_edges(5,0)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   graph.add_edges(3,1)
   print(graph.makeset())
   graph=Graph(6)
   graph.add_edges(4,0)
   graph.add_edges(5,0)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   graph.add_edges(3,1)
   graph.add_edges(4,1)
   print(graph.makeset())

       