class Heap:
   def __init__(self,capacity):
       self.store=[0]*capacity
       self.capacity=capacity
       self.size=0

   def getpindex(self,index):
       return (index-1)//2

   def getlindex(self,index):
       return 2*index+1

   def getrindex(self,index):
       return 2*index+2

   def parent(self,index):
      return self.store[self.getpindex(index)]

   def getlchild(self,index):
       return self.store[self.getlindex(index)]

   def getrchild(self,index):
       return self.store[self.getrindex(index)]

   def isFull(self):
      return self.size==self.capacity

   def hasp(self,index):
       return self.getpindex(index)>=0

   def swap(self,index1,index2):
       self.store[index1],self.store[index2]=self.store[index2],self.store[index1]

   def haslchild(self,index):
      return self.getlindex(index)<=self.size

   def hasrchild(self,index):
      return self.getrindex(index)<=self.size

   def remove(self):
     if self.size==0:
       raise Exception("Empty Heap")
     data=self.store[0]
     self.store[0]=self.store[self.size-1]
     self.size-=1
     self.heapifyDown()
     return data

   def heapifyUp(self):
      if self.size==0:
         raise Exception("Empty heap")
      index=self.size-1
      while (self.hasp(index) and self.parent(index)>self.store[index]):
          pindex=self.getpindex(index)
          self.swap(pindex,index)
          index=pindex

   def heapifyDown(self):
       index=0
       while (self.haslchild(index)):
           sindex=self.getlindex(index)
           if (self.hasrchild(index) and self.getrchild(index)<self.getlchild(index)):
              sindex=self.getrindex(index)
           if (self.store[index]>self.store[sindex]):
              self.swap(sindex,index)
           else:
              break
           index=sindex
              
   def insert(self,data):
       if self.isFull():
          raise Exception("Storage is full")
       self.store[self.size]=data
       self.size+=1
       self.heapifyUp()

if __name__=="__main__":
   h=Heap(8)
   h.insert(12)
   h.insert(5)
   h.insert(10)
   h.insert(8)
   h.insert(10)
   h.insert(7)
   h.insert(1)
   h.insert(-1)
   print(h.store)
   print(h.remove())
   print(h.remove())
   print(h.remove())
   print(h.remove())
   