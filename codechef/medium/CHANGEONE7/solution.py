# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    a=len(A)
    if a==2:
        print(0)
    else:
        minn=min(A)
        sec_minn=float("inf")
        for i in A:
            if i==minn:
                continue
            else:
                sec_minn=min(sec_minn,i)
        print(minn-sec_minn)            