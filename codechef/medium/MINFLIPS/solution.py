# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    c1=0
    c2=0
    for i in A:
        if i==1:
            c1+=1
        else:
            c2+=1