import heapq
def find_min_platform(arr,dep):
   replaced=False
   platform_list=list()
   time_chart=list(zip(arr,dep))
   def sort_time_chart(item):
       return item[1]
   time_chart=sorted(time_chart,key=sort_time_chart)
   platform_list.append(time_chart.pop(0))
   for item in time_chart:
       print(platform_list)
       for i in platform_list:
          if i[1]<item[0] and not replaced:
             index=platform_list.index(i)
             platform_list[index]=item
             replaced=True
       if replaced==False:
          platform_list.append(item)
       print(platform_list)
       replaced=False
   return len(platform_list)


def find_platform(arr,dep):
    platforms=list()
    heapq.heapify(platforms)
    time_chart=list(zip(arr,dep))
    def sorted_chart(item):
        return item[0]
    time_chart=sorted(time_chart,key=sorted_chart)
    count=0
    max=-9
    while time_chart:
        print(platforms)
        train=time_chart.pop(0)
        x,y=train[1],train[0]
        if platforms:
           p=heapq.heappop(platforms)
           if p[0]<train[0]:
              heapq.heappush(platforms,(x,y))
           else:
              count=count+1
              heapq.heappush(platforms,p)
              heapq.heappush(platforms,(x,y))
        else:
           count=count+1
           heapq.heappush(platforms,(x,y))
        if count>max:
           max=count
    print(platforms)
    print(max)
 
        
              
          

if __name__=="__main__":
   print("First Implementation") 
   print(find_min_platform([900,940,950,1100,1500,1800],[910,1200,1120,1130,1900,2000]))
   print("Second Implementation")
   find_platform([900,940,950,1100,800,1500,1800],[910,1200,1120,1130,850,1900,2000])



   
   
       

    