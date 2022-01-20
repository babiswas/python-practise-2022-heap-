import heapq

def heap_operation():
    l=[(1,3),(4,2),(-1,5),(8,10),(-2,5)]
    heapq.heapify(l)
    while l:
        print(heapq.heappop(l))

def heap_insert():
   l=[]
   heapq.heapify(l)
   task_list=[(1,"task1"),(2,"task3"),(-1,"task4"),(0,"task5"),(-3,"task8")]
   for item in task_list:
      heapq.heappush(l,item)
   while l:
      print(heapq.heappop(l))

if __name__=="__main__":
   print("First operation")
   heap_insert()
   print("Second operation")
   heap_operation()
        