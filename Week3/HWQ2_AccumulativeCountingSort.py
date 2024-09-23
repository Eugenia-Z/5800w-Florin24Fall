class Solution:
    def preprocess(nums, k):
        count = [0]*(k+1)
        # count original frequency
        for num in nums:
            count[num] += 1
        
        # count accumulative frequency -> the # of elements that is smaller than nums[i] so far
        for i in range(1, k+1):
            count[i] += count[i-1]
        return count

    def query(count, a, b):
        if a == 1:
            return count[b]
        return count[b] - count[a-1]

if __name__ == "__main__":
    nums = [11, 12, 13, 5, 6, 7]
    sol = Solution
    count = sol.preprocess(nums,15)
    res = sol.query(count, 5, 10)
    print(res)
    