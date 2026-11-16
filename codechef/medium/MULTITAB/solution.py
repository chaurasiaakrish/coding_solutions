# cook your dish here
T=int(input())
for _ in range(T):
    X,Y=map(int,input().split())
    if Y==0:
        print("NO")
    elif X%Y>=3:
        print("YES")
    else:
        print("NO")