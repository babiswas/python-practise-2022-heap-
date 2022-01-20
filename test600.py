def find_max_activity(start,fin):
    stack=list()
    time_chart=list(zip(start,fin))
    def sort_time_chart(item):
        return item[1]
    time_chart=sorted(time_chart,key=sort_time_chart)
    stack.append(time_chart.pop(0))
    while time_chart:
        item=time_chart.pop(0)
        current=stack[-1]
        if current[1]<item[0]:
           stack.append(item)
    print(stack)
    return len(stack)

def find_max_activity2(start,fin):
    time_chart=list(zip(start,fin))
    def sort_time_chart(item):
        return item[1]
    time_chart=sorted(time_chart,key=sort_time_chart)
    current=None
    count=0
    while time_chart:
        item=time_chart.pop(0)
        if current:
           if item[0]>current[1]:
              count=count+1
              current=item
        else:
           current=item
           count=count+1
    return count




if __name__=="__main__":
   print("The maximum activity that will occur:")
   print(find_max_activity([1,3,0,5,8,5],[2,4,6,7,9,9]))
   print("Second test case")
   print(find_max_activity([75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924],[112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]))
   print("Third implementation")
   print(find_max_activity2([1,3,0,5,8,5],[2,4,6,7,9,9]))
   print(find_max_activity2([75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924],[112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]))