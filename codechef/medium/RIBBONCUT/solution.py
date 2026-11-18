# cook your dish here
N=int(input())
for i in range(N):
    for j in range(N,,-1):
        if sum(i,j)==N and i==2*j:
            print("YES")
print("NO")            