# cook your dish here
T=int(input())
for _ in range(T):
    S,R=map(int,input().split())
    freq_S={}
    freq_R={}
    for i in S:
        freq_S[i]=freq_S.get(i,0)+1
    for j in S:
        freq_R[j]=freq_R.get(j,0)+1