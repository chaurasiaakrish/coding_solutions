# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int, input().split()))
    i=0
    while i<len(A)-1:
        summ=A[i+1]-A[i]
        A[i+1]=summ
        A.remove(A[i])
    print (A)    