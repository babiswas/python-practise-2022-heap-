def find_min_distance(arr):
   index_arr=list()
   special_pair=list()
   def find_special_pair(index1,index2,arr):
         if index1==index2 or abs(index1-index2)==1:
            return False
         temp1=arr[index1]
         temp2=arr[index2]
         if temp1>temp2:
            if index1>index2:
               index2=index2+1
               while index2<index1:
                  if arr[index2]>temp2 and arr[index2]<temp1:
                     return False
                  index2=index2+1
            elif index1<index2:
               index1=index1+1
               while index1<index2:
                  if arr[index1]>temp2 and arr[index1]<temp1:
                     return False
                  index1=index1+1
         elif temp2>temp1:
            if index1>index2:
               index2=index2+1
               while index2<index1:
                  if arr[index2]>temp1 and arr[index2]<temp2:
                     return False
                  index2=index2+1
            elif index1<index2:
               index1=index1+1
               while index1<index2:
                  if arr[index1]>temp2 and arr[index1]<temp1:
                     return False
                  index1=index1+1
         return True
   for i in range(len(arr)):
      for j in range(len(arr)):
         index_arr.append((i,j))
   for x,y in index_arr:
      if find_special_pair(x,y,arr):
         special_pair.append((x,y))
   print(special_pair)
   minm=sys.maxsize
   for x,y in special_pair:
      if abs(x-y)<minm:
         minm=abs(x-y)
   return minm

if __name__=="__main__":
   print(find_min_distance([ 0, -10, 5, -5, 1 ]))
   print("Inserting array in tree")
   insert_arr_tree([ 0, -10, 5, -5, 1 ])
  
 