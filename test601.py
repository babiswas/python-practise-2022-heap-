def find_station(n,station):
    arr=[False]*n
    for index in station:
       arr[index]=True
    station=sorted(station)
    maxm=station[0]
    dist=0
    for i in range(len(arr)):
       if arr[i]==False:
          dist=dist+1
       elif arr[i]==True:
          if maxm<(dist+1)/2:
             maxm=dist+1//2
          dist=0
    if arr[n-1]==False:
       if maxm<dist:
          maxm=dist
    return maxm
        

if __name__=="__main__":
   print(find_station(6,[3,1]))
          
    	


















