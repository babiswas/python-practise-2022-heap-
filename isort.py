def isort(arr):
   start=0
   end=len(arr)-1
   for i in range(1,len(arr)):
      fix=arr[i]
      hole=i
      if arr[i]<arr[i-1]:
         while hole-1>=0 and fix<arr[hole-1]:
              arr[hole]=arr[hole-1]
              hole=hole-1
         arr[hole]=fix

if __name__=="__main__":
   arr=[12,10,5,9,19,6,2,21,1]
   isort(arr)
   print(arr)

             

            