def binary_search(arr,start,end,key):
    if start<=end:
       index=(start+end)//2
       if arr[index]==key:
          return index
       elif arr[index]<key:
            start=index+1
            return binary_search(arr,start,end,key)
       elif arr[index]>key:
            end=index-1
            return binary_search(arr,start,end,key)
    return -1


def binary_search_v2(arr,start,end,key):
    while start<=end:
        index=(start+end)//2
        if arr[index]==key:
           return index
        if arr[index]>key:
           end=index-1
        elif arr[index]<key:
           start=index+1
    return -1

if __name__=="__main__":
   l=[11,13,14,21,25,27]
   print(binary_search(l,0,len(l)-1,25))
   print(l)
   for i in l:
     print(binary_search(l,0,len(l)-1,i))
   print("2nd version of the binary search")
   print(binary_search_v2(l,0,len(l)-1,11))
   print(binary_search_v2(l,0,len(l)-1,13))
   print(binary_search_v2(l,0,len(l)-1,14))
   print(binary_search_v2(l,0,len(l)-1,21))
   print(binary_search_v2(l,0,len(l)-1,25))
   print(binary_search_v2(l,0,len(l)-1,27))
       
   