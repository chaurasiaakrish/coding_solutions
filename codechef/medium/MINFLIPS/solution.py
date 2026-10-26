# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    c1=0
    c2=0
    if len(A)%2!=0:
        print(-1)
    else:
        for i in A:
            if i==1:
                c1+=1
            else:
                c2+=1
        req=c1-c2
        if req==0:
            print(0)
        else:
            print(abs(req)//2)