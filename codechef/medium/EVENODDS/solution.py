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
            i+=1
    if count%2==0:
        print(len(A))
    elif count==len(A):
        print(len(A)-1)
    else:
        while i<len(A):
            if A[i]!=0:
                R=i
                size=max(size,R-L)
                L=i+1
                R=L
                i+=1
            else:
                