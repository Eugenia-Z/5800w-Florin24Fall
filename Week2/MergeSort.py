def mergeSort(L):
    # basecase:
    if len(L) < 2:
        return 
    # Divide
    mid = len(L) // 2
    A = L[:mid]
    B = L[mid:]
    
    # Conquer
    mergeSort(A)
    mergeSort(B)
    # Merge
    merge(A,B,L)

def merge(A, B, L):
    i, j = 0, 0
    while i < len(A) and j <len(B):
        if A[i] < B[j]:
            L[i+j] = A[i]
            i += 1
        else:
            L[i+j] = B[j]
            j += 1
    L[i+j:] = A[i:] + B[j:]
    
if __name__ == "__main__":
    L = [3,6,2,6,5,4,8,10]
    mergeSort(L)
    print(L)