# cook your dish here
N=int(input())
A=list(map(int,input().split()))
l=(list(dict.fromkeys(A)))
print(*l)