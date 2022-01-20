import heapq

def find_min_cost(arr):
   heapq.heapify(arr)
   total_cost=0
   while len(arr)>=2:
      cost1=heapq.heappop(arr)
      cost2=heapq.heappop(arr)
      total_cost+=(cost1+cost2)
      heapq.heappush(arr,cost1+cost2)
   print(total_cost)

   

if __name__=="__main__":
   find_min_cost([4,3,2,6])
      
     