def CountingSort(nums):
    # build the count array. length equals the max value of num + 1
    length = max(nums) + 1
    count = [0] * length
    for num in nums:
        count[num] += 1
        
    # update the count array to hold its position -> to be cumulative
    # count[i] tells how many items have digits less than or equal to i at position i
    for i in range(1, length):
        count[i] += count[i-1]
    
    # initialize the output array
    res = [0] * len(nums)
    
    # fillin the output array in reverse order based on the value in countarray
    for num in reversed(nums):
        res[count[num]-1] = num # Place each item in its correct position based on digit i
        count[num] -= 1 # decrease the count in count array after placing the item. 
    return res

if __name__ == "__main__":
    nums = [6, 3, 9, 0, 9, 2, 0, 1, 3, 4, 6, 1, 3]
    print(CountingSort(nums))
            
        