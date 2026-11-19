# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    count=0;i=0
    L=0
    R=0
    size=float("-inf")
    while i< len(A):
        if A[i]%2!=0:
            count+=1
            R=i-1
            i+=1
        else:
            L=i
            size=max(size,(R-L+1))
            R+=1
            i+=1
    if count%2==0:
        print(len(A))
    else:
        print(size)