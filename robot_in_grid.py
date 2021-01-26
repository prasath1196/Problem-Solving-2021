

def find_paths(maze,m,n,i,j,path,pi):

  if i == m -1:
    for k in range(j,n):
      path[pi+k-j] =  maze[i][k]
    print(path)
    return
  if j == n -1:
    for k in range(i,m):
      path[pi+k-i] = maze[k][j]
    print (path)
    return

  path[pi] = maze[i][j]
  find_paths(maze,m,n,i,j+1,path,pi+1)  
  find_paths(maze,m,n,i+1,j,path,pi+1)



m =3
n =3
path = [0 for d in range(m+n-1)]
maze =[[1,2,3],
      [4,5,6],
      [7,8,9]]
i = 0
j = 0
pi = 0
find_paths(maze,m,n,i,j,path,pi)