import bisect

nums = [1,2,4,7,8,10]
left_pos = bisect.bisect_left(nums,6)
right_pos = bisect.bisect_right(nums,4)

bisect.insort(nums, 7)
print(nums)