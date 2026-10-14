# cook your dish here
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    n = list(map(int, input().split()))
    summ=0;high=0;res=float("-inf");low=0;l=0
    for low in range (len(n)):
        summ=summ+n[low]
        while summ>M:
           
            summ=summ-n[high]
            high+=1
        l=(low-high+1)
        res=max(res,l)    
    if res==float("-inf"):
        print(0)
    else:
        print(res)