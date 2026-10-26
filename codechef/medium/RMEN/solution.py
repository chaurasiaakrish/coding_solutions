# cook your dish here
S=input()
s=""
for i in S:
    if i!="#":
        al_bet=121-ord(i)
        s=s+chr(al_bet)
    else:
        continue
print(s)    