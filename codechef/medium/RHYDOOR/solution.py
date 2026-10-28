# cook your dish here
T=int(input())
for _  in range(T):
    N=int(input())
    S=input()
    freq={}
    pas=3;i=0;j=0;res=0
    for i in range(i,pas+i):
        freq[i]=freq.get(i,0)+1
        while freq[i]==3:
            res+=1
            freq[j]-=1
            if freq[j]==0:
                del freq[j]
                j+=1
            else:
                j+=1
        else:
            freq[j]-=1
            if freq[j]==0:
                del freq[j]
                j+=1
            else:
                j+=1
    print(res)            