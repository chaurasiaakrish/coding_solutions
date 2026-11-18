# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    i=0;j=1;summ=float("inf")
    while i<len(A)-1 and j<len(A):
        summ=min(summ,A[i]+A[j])
        i+=1
        j+=1
    print(sum(A)-summ//2)