# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    first_odd = -1
    last_odd = -1
    for i in range(N):
        if A[i] % 2 != 0:
            count += 1
            if first_odd == -1:
                first_odd = i
            last_odd = i
    if count % 2 == 0:
        print(N)
    else:
        len1 = N - 1 - first_odd
        len2 = last_odd
        print(max(len1, len2))
