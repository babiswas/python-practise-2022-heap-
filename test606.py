import heapq
def find_minm_halls(lectures):
    l=list()
    count=0
    heapq.heapify(l)
    def sort_lecture(item):
        return item[0]
    time_chart=sorted(lectures,key=sort_lecture)
    count=0
    while time_chart:
        item=time_chart.pop(0)
        if l:
           cl=heapq.heappop(l)
           if cl[0]<item[0]:
              x,y=item[1],item[0]
              heapq.heappush(l,(x,y))
           else:
              count=count+1
              heapq.heappush(l,cl)
              x,y=item[1],item[0]
              heapq.heappush(l,(x,y))
        else:
           x,y=item[1],item[0]
           heapq.heappush(l,(x,y))
           count=count+1
    return count

def find_min_rooms_v2(lectures):
    start_time=list()
    end_time=list()
    for u,v in lectures:
       start_time.append(u)
       end_time.append(v)
    start_time=sorted(start_time)
    end_time=sorted(end_time)
    pointer1=0
    pointer2=0
    count=0
    completed=0
    started=0
    while pointer1<len(lectures) and pointer2<len(lectures):
          if start_time[pointer1]<end_time[pointer2]:
             started=started+1
             print(f"Classes occupied at time {start_time[pointer1]} is {started-completed}")
             pointer1=pointer1+1
          elif start_time[pointer1]>end_time[pointer2]:
               while start_time[pointer1]>end_time[pointer2]:
                    completed=completed+1
                    print(f"Classes occupied at time {end_time[pointer2]} is {started-completed}")
                    pointer2=pointer2+1
               started=started+1
               print(f"Classes occupied at time {start_time[pointer1]} is {started-completed}")
               pointer1=pointer1+1
    if pointer1==len(lectures):
       while pointer2<len(lectures):
          completed=completed+1
          print(f"Classes occupied at time {end_time[pointer2]} is {started-completed}")
          pointer2=pointer2+1
      

   
   
          
if __name__=="__main__":
   print(find_minm_halls([(0,5),(1,2),(6,10)]))
   print(find_min_rooms_v2([(0,5),(1,2),(6,10)]))
   