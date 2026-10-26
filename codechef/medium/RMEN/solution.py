# cook your dish here
S=input()
s=""
i=0
while i<len(S):
    if "a"<=S[i]<="n":
        value=207-ord(S[i])
        s=s+chr(value)
        i+=1
    elif i+1<len(S) and S[i+1]=='#':
        value=233-ord(S[i])
        s=s+chr(value)
        i+=2
print(s)        
    