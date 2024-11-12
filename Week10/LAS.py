def las_recursion(A):
    n = len(A)
    memo_up = [-1] * n
    memo_down = [-1] * n
    
    def Vu(j):
        if memo_up[j] != -1:
            return memo_up[j]
        max_length =  1
        for k in range(j+1, n):
            if A[k] < A[j]:
                max_length = max(max_length, 1 + Vd(k))
            memo_up[j] = max_length
        return max_length

    def Vd(j):
        if memo_down[j] != -1:
            return memo_down[j]
        max_length =  1
        for k in range(j+1, n):
            if A[k] > A[j]:
                max_length = max(max_length, 1 + Vu(k))
            memo_down[j] = max_length
        return max_length
    
    # Calculate the maximum LAS by considering both up and down stats for each index
    las_length = 0
    for j in range(n):
        las_length = max(las_length, Vu(j), Vd(j))
    return las_length

def las_bottom_up(A):
    n = len(A)
    # init tables
    Vu = [1] * n
    Vd = [1] * n
    
    # Fill the tables from the end to the beginning
    for j in range(n-2, -1, -1):
        for k in range(j+1, n):
            if A[k] < A[j]:
                Vu[j] = max(Vu[j], Vd[k] + 1)
            elif A[k] > A[j]:
                Vd[j] = max(Vd[j], Vu[k] + 1)
    las = max(max(Vu), max(Vd))
    return las

def las_one_pass(A):
    n = len(A)
    inc = 1
    dec = 1
    for i in range(1, n):
        if A[i] > A[i-1]:
            inc = dec + 1
        elif A[i] < A[i-1]:
            dec = inc + 1
    return max(inc, dec)
# Driver Code
A = [10, 22, 9, 33, 49, 50, 31, 60]
print("Length of Longest alternating subsequence is",
      las_recursion(A))