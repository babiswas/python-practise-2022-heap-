import heapq

def find_k_largest(arr,k):
   l=list()
   index=0
   stack=list()
   heapq.heapify(l)
   for i in arr:
      heapq.heappush(l,-1*i)
   while l:
     index=index+1
     item=heapq.heappop(l)
     item=item*-1
     stack.append(item)
     if index==k:
       break
   return stack[-1]

if __name__=="__main__":
   arr=[12,1,20,5,9,10,12,16,11]
   print("Result obtained from max heap")
   print(find_k_largest(arr,3))
   print("Result obtained from sorting")
   myarr=sorted(arr,reverse=True)
   print(myarr[2])
   print(myarr)
   
   
      
   