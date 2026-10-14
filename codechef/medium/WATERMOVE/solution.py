# cook your dish here
T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    ans1=sum(A[:K+1])
    maxx