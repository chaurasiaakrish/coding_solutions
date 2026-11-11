# cook your dish here
T=int(input())
for _  in range(T):
    N,D=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    case1=sum(A)+D
    case2=sum(B)+D
    case3=case1+case2
    summ = sum(min(a,b)for a, b in zip(A,B))   
    case4=summ+2*D
    print(min(case1,case2,case3,case4))