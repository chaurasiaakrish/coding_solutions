# cook your dish here
T=int(input())
for _ in range(T):
    A=int(input())
    summ=0
    while A>0:
        rem=A%10
        summ=summ+rem
        A=A//10
    if summ%10==0:
        print("Valid")
    else:
        print("Invalid")