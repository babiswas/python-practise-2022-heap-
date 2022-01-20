def partition(arr,start,end):
    wall=start-1
    fix=arr[end-1]
    for i in range(start,end-1):
       if arr[i]<fix:
          wall=wall+1
          arr[wall],arr[i]=arr[i],arr[wall]
    wall=wall+1
    arr[wall],arr[end-1]=arr[end-1],arr[wall]
    return wall

def partition_m(arr,start,end,pivot):
   wall=start-1
   fix=pivot
   for i in range(start,end):
       if arr[i]<pivot:
          wall=wall+1
          arr[wall],arr[i]=arr[i],arr[wall]
   print(wall)
   print(arr)


def qsort(arr,start,end):
   if start<end:
      index=partition(arr,start,end)
      print(index)
      qsort(arr,start,index)
      qsort(arr,index+1,end)
   

if __name__=="__main__":
   arr=[12,1,2,21,0,5,4,3]
   partition(arr,0,len(arr))
   print(arr)
   qsort(arr,0,len(arr))
   print("After sorting")
   print(arr)
         