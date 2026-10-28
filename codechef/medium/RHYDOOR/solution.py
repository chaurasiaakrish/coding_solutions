# cook your dish here
T=int(input())
for _  in range(T):
    N=int(input())
    S=input()
    i=0
    pas=3;op=0
    while i<len(S):
        if S[i:pas+i]=="AAA" or S[i:pas+i]=="BBB":
            op+=1
            i=i+pas
        else:
            i+=1
    print(op)    