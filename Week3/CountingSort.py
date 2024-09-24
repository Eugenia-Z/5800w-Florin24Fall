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
        res[count[num]-1] = num
        count[num] -= 1
    return res

if __name__ == "__main__":
    nums = [1,1,4,1,2,3,5,6,4]
    print(CountingSort(nums))
            
        
        