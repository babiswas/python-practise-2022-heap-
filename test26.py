import heapq
def find_k_closest(arr,k,x):
   l=list()
   heapq.heapify(l)
   for i in arr:
     print(i)
     if i>=x:
       a,b=-1*(i-x),i
     elif i<x:
       a,b=1*(i-x),i
     heapq.heappush(l,(a,b))
     print(l)
     if len(l)>k:
        heapq.heappop(l)
   print("Displaying the k closest element:")
   while l:
     print(heapq.heappop(l)[1])

if __name__=="__main__":
   arr=[5,6,7,8,9]
   find_k_closest(arr,3,7)
      
       
   
   