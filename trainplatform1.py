def find_min_platforms(arr,dep):
    arr=sorted(arr)
    dep=sorted(dep)
    print(arr)
    print(dep)
    arrival=0
    depart=0
    pointer1=0
    pointer2=0
    platforms=0
    while pointer1<len(arr) and pointer2<len(arr):
        if arr[pointer1]>dep[pointer2]:
             while arr[pointer1]>dep[pointer2]:
                 depart=depart+1
                 platforms=arrival-depart
                 print(f"At time {dep[pointer2]} platforms occupied {platforms}")
                 pointer2=pointer2+1
             arrival=arrival+1
             platforms=arrival-depart
             print(f"At time {arr[pointer1]} platforms occupied {platforms}")
             pointer1=pointer1+1
        elif arr[pointer1]<dep[pointer2]:
             arrival=arrival+1
             platforms=arrival-depart
             print(f"At time {arr[pointer1]} platforms occupied {platforms}")
             pointer1=pointer1+1
    if pointer1==len(arr):
      while pointer2<len(arr):
         depart=depart+1
         platforms=arrival-depart
         print(f"At time {dep[pointer2]} platforms occupied {platforms}")
         pointer2=pointer2+1

      
if __name__=="__main__":
   find_min_platforms([900,940,950,1100,1500,1800],[910,1200,1120,1130,1900,2000])
   

        
        