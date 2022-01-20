import heapq
import copy
def find_pairs(l):
   master_list=[]
   m=list()
   heapq.heapify(l)
   m.append(heapq.heappop(l))
   while l:
     item=heapq.heappop(l)
     print((item,copy.deepcopy(m)))
     m.append(item)
   for i in master_list:
      print(i)

if __name__=="__main__":
   find_pairs([2,5,3,6,7,9,1])
   