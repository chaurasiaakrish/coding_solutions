# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    large=N//4
    small=N-large
    if small>=2:
        print("YES")
    else:
        print("NO")