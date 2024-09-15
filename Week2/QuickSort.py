def quickSort(L):
    # base case:
    if len(L)<2:
        return L[:]
    
    # Divide
    pivot = L[-1] # pivot is the last element
    LT = [e for e in L if e < pivot]
    ET = [e for e in L if e == pivot]
    GT = [e for e in L if e > pivot]
    
    # Conquer
    A = quickSort(LT)
    B = quickSort(GT)
    
    return A + ET + B

if __name__ == "__main__":
    L = [3,6,2,6,5,4,8,10]
    result = quickSort(L)
    print(result)