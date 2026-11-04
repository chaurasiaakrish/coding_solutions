# cook your dish here
N=int(input())
if N<5:
    print(N)
else:
    rem=N%5
    print(rem+(N-rem))