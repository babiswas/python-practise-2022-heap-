import heapq
def issafe(x,y,mat):
   if x<0 or x>=len(mat):
      return False
   if y<0 or y>=len(mat):
      return False
   return True
    
def dkstra(mat,src_x,src_y):
   l=list()
   heapq.heapify(l)
   visited=[[False for i in range(len(mat))] for i in range(len(mat))]
   dx=[1,0,1]
   dy=[0,1,1]
   cost=mat[src_x][src_y]
   all_vertices=len(mat)*len(mat)
   while all_vertices:
        for i in range(3):
           X=src_x+dx[i]
           Y=src_y+dy[i]
           if issafe(X,Y,mat):
              heapq.heappush(l,(cost+mat[X][Y],(X,Y)))
        data=heapq.heappop(l)
        src_x=data[1][0]
        src_y=data[1][1]
        if visited[src_x][src_y]==False:
           mat[src_x][src_y]=data[0]
           visited[src_x][src_y]=True
        cost=data[0]
        all_vertices=all_vertices-1
   print(mat)


if __name__=="__main__":
   mat=[[1,2,3],[4,8,2],[1,5,3]]
   dkstra(mat,0,0)
   
   
        
  