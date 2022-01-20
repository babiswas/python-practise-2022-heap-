import heapq

def find_k_smallest(arr,k):
   l=list()
   heapq.heapify(l)
   for i in arr:
      heapq.heappush(l,-1*i)
      if len(l)>k:
         print(-1*heapq.heappop(l))
   print(f"Displaying the {k} th smallest element")
   print(-1*heapq.heappop(l))
   while l:
     heapq.heappop(l)
   print(l)

if __name__=="__main__":
   arr=[12,6,4,12,4,3,1]
   find_k_smallest(arr,3)
   brr=[6,1,16,14,2,0,5]
   find_k_smallest(brr,3)
   
   