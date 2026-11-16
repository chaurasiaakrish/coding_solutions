# cook your dish here
T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    summ=sum(A)
    if summ//(N+K)==K:
        print("yes")
    else:
        print("no")