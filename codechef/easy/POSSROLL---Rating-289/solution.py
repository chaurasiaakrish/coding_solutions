# cook your dish here
flag=False
X,K,Y=map(int,input().split())
if Y<=X*K and Y%K==0:
    print("YES")
else:
    print("NO")
    
    
    