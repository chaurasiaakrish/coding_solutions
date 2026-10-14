# cook your dish here
T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    ans = max(A[-1], A[0] + A[1])
    print(ans)