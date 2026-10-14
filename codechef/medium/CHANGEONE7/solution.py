# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    a=len(A)
    if a==2:
        print(0)
    else:
        print(max(A)-min(A))
    