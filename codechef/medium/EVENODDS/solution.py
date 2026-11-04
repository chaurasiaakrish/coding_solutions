# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    L=0;R=0
    for i in A:
        if i%2!=0:
            