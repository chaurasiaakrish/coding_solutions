# cook your dish here
T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    S=input()
    alarm=0;i=0
    while i in range(len(S)):
        if S[i]=="1":
            alarm+=1
            i=i+K+1
        else:
            i+=1
    print(alarm)        