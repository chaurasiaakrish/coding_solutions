# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int, input().split()))
    while len(A)>1:
        for i in range(len(A)-1):
        summ=nums[i+1]-nums[i]
        nums.replace(nums[i+1],summ)
        nums.remove(nums[i])
    print (A)    