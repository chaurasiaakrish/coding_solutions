# cook your dish here
T=int(input())
for _   in range(T):
    N,M=map(int,input().split())
    grid = []
    l=[]
    for _ in range(N):
        row=list(map(int, input().strip()))
        grid.append(row)
    for i in range(N):
        for j in range(M):
            if grid[i][j]==1:
                l.append([i+1,j+1])
    if len(l)==0:
        print(0)
    else:
        print(l[0][0]*l[-1][1])