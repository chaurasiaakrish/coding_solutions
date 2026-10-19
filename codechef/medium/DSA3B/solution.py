def max_sum_subarray_k(arr, n, k):
  

    # Step 1: First window
    

    # Step 2: Slide the window
   
 
 
  
# -- Input handling (Dont edit below code) --

T = int(input())
    
for _ in range(T):
    N, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res=max_sum_subarray_k(arr, len(arr), k)
    print(*res)
