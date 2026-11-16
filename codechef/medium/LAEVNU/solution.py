# cook your dish here
S=input()
l=[]
for i in S:
    if i.isdigit():
        l.append(i)
flag=False
for j in l:
    if int(j)%2==0:
        flag=True
        break
if flag==False:
    print(-1)
else:
    l.sort()
    if int(l[0])%2==0:
        print(int("".join(l[::-1])))
    else:
        for i in l:
            if 