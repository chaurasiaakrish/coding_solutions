# cook your dish here
T=int(input())
for _   in range(T):
    N,M=map(int(input().split()))
    grid = []
    for _ in range(N):
    # Read the string, split it into characters, and convert each to an int
    row = list(map(int, input().strip()))
    grid.append(row)