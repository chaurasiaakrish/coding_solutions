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
        min_row = min(coord[0] for coord in l)
        max_row = max(coord[0] for coord in l)
        min_col = min(coord[1] for coord in l)
        max_col = max(coord[1] for coord in l)
        height = max_row - min_row + 1
        width = max_col - min_col + 1
        print(height*width)