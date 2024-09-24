# a numpy implementation of radix sort
import numpy as np

def RadixSort(B):
    n, d = B.shape # : n is the number of items, d: # of digits per item
    
    # loop over the digit starting from the least significant digit
    for i in reversed(range(d)):
        A = B.copy()
        
        # initialize the counting array
        k = np.zeros(10, dtype=int) # Create a counting array k of size 10 to count occurrences of each digit (0-9)
        
        # count occurences of digits:
        for j in range(n):
            k[A[j,i]] += 1 # count how many times each digit appears at the i-th position     
        
        # compute cumulative counts:
        k = k.cumsum() # convert the count array into cumulative counts(prefix sum)
        
        # reorder the array based on the current digit:
        for j in reversed(range(n)):
            B[k[A[j,i]] - 1, :] = A[j]
            k[A[j,i]] -= 1
    
    return B


if __name__ == "__main__":  
    test_array = np.array([
    [1, 4, 3],  # Item 1
    [1, 3, 5],  # Item 2
    [2, 4, 3],  # Item 3
    [1, 3, 3],  # Item 4
    [2, 3, 3]   # Item 5
], dtype=int)

    print("Original array:", test_array)
    sorted_array = RadixSort(test_array)
    print("Sorted array:", sorted_array)   