import heapq
def k_largest_element(arr,k):
    l=list()
    heapq.heapify(l)
    for i in arr:
       heapq.heappush(l,i)
       if len(l)>k:
          heapq.heappop(l)
    while l:
      print(heapq.heappop(l))

if __name__=="__main__":
   arr=[12,5,4,3,1,10,16,13]
   k_largest_element(arr,3)
   arr=[12,5,4,3,1,10,16,13]
   print(sorted(arr))
        