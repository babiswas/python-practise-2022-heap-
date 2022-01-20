class Item:
   def __init__(self,parent):
       self.parent=parent
       self.rank=0


class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=[]

   def add_edges(self,u,v,w):
       self.graph.append((u,v,w))

   def find(self,u,arr):
       if arr[u].parent!=u:
          arr[u].parent=self.find(arr[u].parent,arr)
       return arr[u].parent

   def union(self,u,v,arr):
       index1=self.find(u,arr)
       index2=self.find(v,arr)
       if index1==index2:
          return 
       else:
          if arr[index1].rank>arr[index2].rank:
             arr[index2].parent=index1
             arr[index1].rank+=1
          elif arr[index2].rank>=arr[index1].rank:
             arr[index1].parent=index2
             arr[index2].rank+=1

   def makeset(self):
      edge_list=list()
      arr=[Item(i) for i in range(self.vertex)]
      def get_item(obj):
         return obj[2]
      self.graph=sorted(self.graph,key=get_item)
      for u,v,w in self.graph:
          index1=self.find(u,arr)
          index2=self.find(v,arr)
          if index1!=index2:
             self.union(index1,index2,arr)
             edge_list.append((u,v,w))
          else:
             pass
      print(edge_list)

if __name__=="__main__":
   graph=Graph(9)
   graph.add_edges(0,7,8)
   graph.add_edges(0,1,4)
   graph.add_edges(7,1,11)
   graph.add_edges(1,2,8)
   graph.add_edges(2,3,7)
   graph.add_edges(3,4,9)
   graph.add_edges(5,4,10)
   graph.add_edges(3,5,14)
   graph.add_edges(2,5,4)
   graph.add_edges(6,5,2)
   graph.add_edges(8,6,6)
   graph.add_edges(8,2,2)
   graph.add_edges(7,6,1)
   graph.add_edges(7,8,7)
   graph.makeset()
   
          
