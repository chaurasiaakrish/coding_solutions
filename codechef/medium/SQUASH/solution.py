# cook your dish here
T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    S=input()
    i=0;j=1;count=0
    while j<len(S):
        if S[i]==S[j]:
            count+=1
        else:
            i+=1
            j+=1