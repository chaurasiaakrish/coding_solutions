# cook your dish here
T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    n=input().strip()
    m=input().strip()
    l=[]
    for i in n:
        if i in m:
            l.append("L")
        else:
            l.append("R")
    j=0;count=1;res=0
    while j<len(l):
        if j>0 and l[j]==l[j-1]:
            count+=1
            
            j+=1
        else:
            count=1
            j+=1
        res=max(res,count)    
    print(res)        