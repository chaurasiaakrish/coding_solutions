# cook your dish here
s1=input()
s2=input()
c1=""
c2=""
freq1={}
freq2={}
for i in s1:
    if i.isalpha():
        c1+=i.lower()
    else:
        c1+=" "
for j in s2:
    if j.isalpha():
        c2+=j.lower()
    else:
        c2+=" "        
for k in c1.split():
    freq1[k]=freq1.get(k,0)+1
for l in c2.split():
    freq2[l]=freq2.get(l,0)+1    
if freq1==freq2:
    print("The sentences are anagrams.")
else:
    print("The sentences are not anagrams.")