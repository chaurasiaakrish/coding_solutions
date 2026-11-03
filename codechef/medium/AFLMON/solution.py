# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    great=0;less=0;ans=0;i=0;j=i+1;res=0
    while i <len(A):
        while j<len(A):
            if A[i]>=A[j]:
                great+=1
                j+=1
            else:
                less+=1
                j+=1
        if great > less:
            res+=1
        i+=1  
    print(res)    
              