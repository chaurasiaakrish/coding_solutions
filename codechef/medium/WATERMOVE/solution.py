# cook your dish here
T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    if K >= N-1:
        print(max(A))
    else:
        print(min(max(A), sum(A[:K + 1])))