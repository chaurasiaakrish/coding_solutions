# cook your dish here
S=input()
s=""
i=0
while i<len(S):
    if S[i]=="#":
        i+=1
    elif "a"<=S[i]<="n":
        value=207-ord(S[i])
        s=s+chr(value)
        i+=1
    else:
        value=233-ord(S[i])
        s=s+chr(value)
        i+=1
print(s)        
    