import heapq

def k_sorted(arr,k):
    l=list()
    heapq.heapify(l)
    index=0
    for i in arr:
       index=index+1
       heapq.heappush(l,i)
       if index==k+1:
          print(heapq.heappop(l))
          index=index-1
    print("Completed array traversal")
    while l:
      print(heapq.heappop(l))

if __name__=="__main__":
   arr=[6,5,3,2,8,10,9]
   k_sorted(arr,3)
       
       