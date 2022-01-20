import heapq
def k_largest_element(arr,k):
    l=list()
    heapq.heapify(l)
    for i in arr:
       heapq.heappush(l,i)
       if len(l)>k:
          heapq.heappop(l)
    print(heapq.heappop(l))
    while l:
       heapq.heappop(l)

if __name__=="__main__":
   arr=[14,12,1,11,5,3,23,2]
   k_largest_element(arr,3)
   brr=[14,12,1,11,5,3,23,2]
   print(sorted(brr))
    