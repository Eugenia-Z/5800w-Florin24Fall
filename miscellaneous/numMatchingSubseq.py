from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s, words):
        # step 1: build dict for s
        char_to_index = defaultdict(list)
        for index, char in enumerate(s):
            char_to_index[char].append(index)
        res = 0
        # step 2: go through each word and search for the next index to check for matching
        for word in words:
            i, j = 0, 0  # pointers to traverse s, word
            is_subsequence = True  # flag variable to keep track of whether there is a subsequence
            # traverse one word at a time
            while j < len(word):
                char = word[j]
                
                # case that char not in the dict at all
                if char not in char_to_index:
                    is_subsequence = False 
                    break
                
                # case that chat char in the dict, we gotta find the next index that right behind it
                # Binary search to find the left-bound index that is >= i
                index = self.left_bound(char_to_index[char], i)
                
                # If no such index exisits
                if index == len(char_to_index[char]):
                    is_subsequence = False
                    break
                
                # such index exists, now update the next character in s after the found index
                i = char_to_index[char][index] + 1
                # move to the next character in the word
                j += 1
                    
        
            # If j completes matching, then the word is a subsequence of s
            if is_subsequence:
                res += 1
        return res

    def left_bound(self, arr, target):
        left, right = 0, len(arr)-1
        while left <= right:
            mid = left + (right-left) // 2
            if arr[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
if __name__ == "__main__":
    sol = Solution()
    s = "abcde"
    words = ["a","bb","acd","ace"]
    res = sol.numMatchingSubseq(s, words)
    print(res)