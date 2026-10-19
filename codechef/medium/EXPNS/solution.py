# cook your dish here
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if Y*30<=X:
        print("YES")
    else:
        print("NO")