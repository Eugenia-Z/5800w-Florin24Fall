def counting_sort(arr, exp):
    n = len(arr)
    output =[0] * n
    count = [0] * 10
    
    # count the occurrence of each digit
    for i in range(n):
        index = (arr[i]//exp) % 10
        count[index] += 1
    
    # update the count array so that it contains the actual position of the digit
    for i in range(1, 10):
        count[i] += count[i-1]
        
    # build the output array:
    for i in range(n-1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index]-1] = arr[i]
        count[index] -= 1
    
    # copy the sorted values back to arr
    for i in range(n):
        arr[i] = output[i]
        
def radix_sort(arr):
    # find the maximum number to knoe the number of each digit
    max_num = max(arr)
    
    # apply counting sort to each digit (exp is 10^i where i is the digit position)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
  
if __name__ == "__main__":      
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original array:", arr)
    radix_sort(arr)
    print("Sorted array:", arr)