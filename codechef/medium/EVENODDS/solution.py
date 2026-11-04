# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    count=0
    for i in A:
        if i%2!=0:
            count+=1
    if count%2==0:
        print(len(A))
    else:
        