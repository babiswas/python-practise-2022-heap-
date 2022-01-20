import heapq

def find_sum(arr,k):
    l=list()
    heapq.heapify(l)
    for i in range(len(arr)):
       heapq.heappush(l,(-1*arr[i],i))
       if len(l)>k:
          heapq.heappop(l)
    value,index=heapq.heappop(l)
    return index,-1*value


if __name__=="__main__":
   arr=[12,2,5,7,3,1,8,10]
   index1,value=find_sum(arr,3)    
   index2,value=find_sum(arr,6)
   sum=0
   if index1<index2:
      for i in range(index1+1,index2):
         sum+=arr[i]
   elif index2>index1:
      for i in range(index2+1,index1):
         sum+=arr[i]
   print(sum)
   index=min(index1,index2)
   for i in range(index1+1,index2+1):
      print(arr[i])
   print(arr)
   arr=sorted(arr)
   print(arr)

         
          
       