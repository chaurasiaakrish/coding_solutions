# cook your dish here
T=int(input())
for _ in range(T):
    X,Y=map(int,input().split())
    if X==Y and X!=0 and Y!=0:
        print("YES")
    else:
        print("NO")