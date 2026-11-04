# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    count=0
    L=0
    R=0
    size=float("-inf")
    for i in range(len(A)):
        if A[i]%2!=0:
            count+=1
            R=i
            size=max(size,(R-L+1))
            L=R
    if count%2==0:
        print(len(A))
    else:
        print(size)