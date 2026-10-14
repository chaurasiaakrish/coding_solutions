# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    a=len(A)
    if a==2:
        print(0)
    else:
        A.sort()
        ans1=A[-1]-A[1]
        ans2=A[-2]-A[0]
        print(min(ans1,ans2))    