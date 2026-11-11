# cook your dish here
T=int(input())
for _  in range(T):
    N,D=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    case1=sum(A)+D
    case2=sum(B)+D
    case3=case1+case2
    i=0;j=0;summ=0
    while i>len(A) and j>len(B):
        summ=summ+min(i,j)
        i+=1
        j+=1
    case4=summ+2*D    
    print(min(case1,case2,case3,case4))