import heapq
def find_highest_frequency(arr):
    l=list()
    heapq.heapify(l)
    m=dict()
    for i in arr:
      val=m.get(i,0)
      m[i]=val+1
    for key,val in m.items():
       heapq.heappush(l,(-1*val,key))
    while l:
       item=heapq.heappop(l)
       print(f"({item[0]*-1},{item[1]})")


if __name__=="__main__":
   arr=[1,1,1,3,2,2,4]
   find_highest_frequency(arr)
