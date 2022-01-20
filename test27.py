import heapq
def freq_sort(arr,k):
   m=dict()
   for i in arr:
      val=m.get(i,0)
      m[i]=val+1
   l=list()
   heapq.heapify(l)
   for key,val in m.items():
      heapq.heappush(l,(val,key))
      if len(l)>k:
         heapq.heappop(l)
   while l:
     print(heapq.heappop(l))
   print(m)

if __name__=="__main__":
   arr=[1,1,1,3,2,2,4]
   freq_sort(arr,3)
  