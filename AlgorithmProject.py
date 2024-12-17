def counting_sort(A):
    
    if len(A) == 0:
        return A  
    
    k = max(A) 
    n = len(A)
    
    
    C = [0] * (k + 1)  
    
    
    for i in range(n):
        C[A[i]] += 1
    
    
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    
   
    B = [0] * n  
    for i in range(n - 1, -1, -1): 
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    
    
    for i in range(n):
        A[i] = B[i]
    
    return A


arr = [4, 2, 2, 8, 3, 3, 1]  
sorted_arr = counting_sort(arr) 
print("Sorted array:", sorted_arr)
