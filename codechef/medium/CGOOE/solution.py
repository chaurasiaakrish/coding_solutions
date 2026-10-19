# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    A=list(map(int,input().split))
    count=0
    for i in range(len(A)-1,-1,-1):
        if i>=5:
            j=i-5
            while j<i:
                if nums[i]<nums[j]:
                    continue
                else:
                    count+=1
        else:
            j=0
            while j<i:
                if nums[i]<nums[j]:
                    continue
                else:
                    count+=1
print(len(A)-count)                    
                    