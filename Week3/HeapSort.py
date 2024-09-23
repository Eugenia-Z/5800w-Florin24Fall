class Solution:
    def heapsort(self, nums):
        # max-heapify function
        def max_heapify(heap_size, index):
            left,right = 2*index, 2*index + 1
            largest = index # initialize largest as the root
            
            # see if left child of root exisits and is greater than root
            if left < heap_size and nums[left] > nums[largest]:
                largest = left
            # see if right child of root exisits and is greater than root
            if right < heap_size and nums[right] > nums[largest]:
                largest = right
            
            if largest != index:
                # change the root, if needed
                nums[largest], nums[index] = nums[index], nums[largest]
                max_heapify(heap_size, largest) # largest is the index of previously largest child
        
        # max_heapify the original array O(n) -> bottom up slightly more efficient
        for i in range(len(nums)//2 - 1, -1, -1):
            max_heapify(len(nums), i)
            
        
        # heap sort
        for i in range(len(nums)-1, 0, -1):
            # swap the last element with the first element (max element)
            nums[0], nums[i] = nums[i], nums[0]
            
            # now the heap property is violated, we have to re-heapify, with one element less each iteration
            max_heapify(i, 0)

if __name__ == "__main__":
    arr = [12, 1, 13, 5, 6, 7]
    sol = Solution()
    sol.heapsort(arr)
    print("Sorted array is: ", arr)