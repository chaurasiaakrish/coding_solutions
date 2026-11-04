# cook your dish here
import math
T=int(input())
for _ in range(T):
    X,Y,D=map(int,input().split())
    if abs(X-Y)<=D:
        print(max(X,Y))
    else:
        print(math.lcm(X,Y))