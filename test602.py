def find_indices_diff(arr):
    index1=0
    index2=0
    test=True
    min=99999
    for i in range(len(arr)):
       index1=i
       if i+1<len(arr):
          for j in range(i+1,len(arr)):
               if arr[i]<=arr[j]:
                  index1=index1+1
                  while index1<j:
                      if arr[index1]<arr[j] and arr[index1]>arr[i]:
                         test=False
                         break
                      index1=index1+1
                  if test and i+1!=j:
                     if min>abs(i-j):
                        min=abs(i-j)
       test=True     
    return min


if __name__=="__main__":
   print(find_indices_diff([0, -10, 5, -5, 1]))
   

                  
             
          
             