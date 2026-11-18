# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    A.sort()
    summ=sum(A)
    summ=summ-(A[0]/2+A[1]/2)
    print(int(summ))
    