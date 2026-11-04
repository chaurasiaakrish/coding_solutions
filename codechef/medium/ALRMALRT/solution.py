# cook your dish here
import math
T = int(input())
for _ in range(T):
    X, Y, D = map(int, input().split())
    ans1 = float('inf')
    for k in range(1, Y + 1):
        t1 = k * X
        if t1 >= Y and (t1 % Y) <= D:
            ans1 = t1
            break
    ans2 = float('inf')
    for m in range(1, X + 1):
        t2 = m * Y
        if t2 >= X and (t2 % X) <= D:
            ans2 = t2
            break
            
    print(min(ans1, ans2))
