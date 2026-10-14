# cook your dish here
T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort(reverse=True)
    print(sum(A[:K+1]))