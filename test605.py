import sys
def find_last_seen_element(arr):
   index=dict()
   for i in range(len(arr)):
     index[arr[i]]=i
   min=sys.maxsize
   x,y=0,0
   for index,val in index.items():
     if min>val:
        min=val
        x,y=val,index
   print(x,y)

if __name__=="__main__":
   find_last_seen_element([10,30,20,10,20])
     