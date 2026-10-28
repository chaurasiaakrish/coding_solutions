# cook your dish here
T=int(input())
for _  in T:
    N=int(input())
    S=input()
    freq={}
    pass=0
    for i in S:
        freq[i]=freq.get(i,0)+1
    for i in freq:
        
        