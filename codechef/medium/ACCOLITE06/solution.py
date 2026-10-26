# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    if sum(A)%2!=0:
        print("NO")
    else:
        print("YES")
    