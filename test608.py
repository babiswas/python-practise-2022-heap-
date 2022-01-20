def form_pairs(arr,start,end,key,l):
    if start<=end:
       index=(start+end)//2
       if arr[index]==key:
          end=index-1
       elif arr[index]>key:
          form_pairs(arr,start,end-1,key,l)
       elif arr[index]<key:
          if (key,arr[index]) not in l:
             l.append((key,arr[index]))
          form_pairs(arr,start,end-1,key,l)
          form_pairs(arr,index+1,end,key,l)


def form_pairsv2(arr,start,end,key):
    while start<=end:
        index=(start+end)//2
        if arr[index]==key:
           return index
        elif arr[index]<key:
           start=index+1
        elif arr[index]>key:
           end=index-1
       
        

def find_pairs(arr):
    arr=sorted(arr)
    l=dict()
    for i in arr:
       index=form_pairsv2(arr,0,len(arr)-1,i)
       l[i]=index
    for key in l.keys():
      m=[key]*len(arr[:l[key]])
      print(list(zip(m,arr[:l[key]])))
         
    
    
if __name__=="__main__":
   find_pairs([12,5,7,14,10,3])
    