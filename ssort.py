def ssort(arr):
   for i in range(len(arr)):
     if i+1<len(arr):
        for j in range(i+1,len(arr)):
           if arr[i]>arr[j]:
              arr[i],arr[j]=arr[j],arr[i]

if __name__=="__main__":
   arr=[12,11,5,4,2,18,10,9]
   ssort(arr)
   print(arr)
   
  