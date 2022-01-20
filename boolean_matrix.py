def find_region(visited,matrix,x,y):
    counter=0
    queue=list()
    dx=[1,1,1,0,0,-1,-1,-1]
    dy=[1,0,-1,1,-1,1,0,-1]
    queue.append((x,y))
    visited[x][y]=True
    while queue:
       m=queue.pop(0)
       counter=counter+1
       for i in range(8):
           X=m[0]+dx[i]
           Y=m[1]+dy[i]
           if issafe(X,Y,matrix,4,5):
              if visited[X][Y]==False:
                  queue.append((X,Y))
                  visited[X][Y]=True
    return counter
       
def issafe(x,y,matrix,m,n):
    if x<0 or x>=m:
         return False
    if y<0 or y>=n:
         return False
    if matrix[x][y]==0:
         return False
    return True
        
        
def find_largest_region():
    max_area=-1
    visited=[[False for i in range(5)] for j in range(4)]
    matrix=[[0,0,1,1,0],[1,0,1,1,0],[0,1,0,0,0],[0,0,0,0,1]]
    for i in range(4):
      for j in range(5):
        if not visited[i][j] and matrix[i][j]==1:
           area=find_region(visited,matrix,i,j)
           if max_area<area:
              max_area=area
    return max_area

if __name__=="__main__":
   print(find_largest_region())
           
    