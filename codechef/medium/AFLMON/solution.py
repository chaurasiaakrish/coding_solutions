# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    A.sort()
    j=0;res=0
    for i in range(len(A)):
        while j < len(A) and A[j] <= A[i]:
            j += 1
        low = j
        great = len(A) - j
        if low > great:
            res += 1
    print(res)        