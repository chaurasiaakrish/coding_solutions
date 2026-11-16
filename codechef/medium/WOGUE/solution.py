# cook your dish here
T=int(input())
for _ in range(T):
    S=input()
    R=input()
    i=0;j=0
    M=""
    while i<len(S) and j<len(R):
        if S[i]==R[j]:
            M+='G'
            i+=1
            j+=1
        else:
            M+='B'
            i+=1
            j+=1
    print(M)        