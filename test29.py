import heapq

def find_k_closest(arr,k):
   l=list()
   heapq.heapify(l)
   print(arr)
   for u,v in arr:
     heapq.heappush(l,(-1*(u**2+v**2),(u,v)))
     if len(l)>k:
        heapq.heappop(l)
   while l:
     print(heapq.heappop(l)[1])

if __name__=="__main__":
   arr=[(1,3),(-2,2),(5,8),(0,1)]
   find_k_closest(arr,3)
   