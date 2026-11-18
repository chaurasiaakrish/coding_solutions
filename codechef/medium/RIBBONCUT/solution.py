# cook your dish here
N=int(input())
flag=True
for i in range(N):
    for j in range(N,0,-1):
        if i+j==N and i==2*j:
            print("YES")
            break
        else:
            flag=False