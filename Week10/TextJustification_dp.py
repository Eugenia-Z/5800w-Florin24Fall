# DP solution to text justification problem with cost function defined
def text_justification (words, max_width):
    n = len(words)
    
    # Precompute the cost for each line from word i to word j, which is the combination of actual word length and the space dictated by j-i
    def compute_cost(i, j):
        length = sum(len(words[k]) for k in range(i, j+1)) + (j-i) # words and space between them
        if length > max_width:
            return float('inf') # Exceeds line width, invalid
        else:
            return (max_width - length) ** 3
    
    # init DP table:
    # dp[i] represents the minimum total cost for justifying the paragraph from the word i to the end
    dp = [float('inf')] * (n+1)
    # base case: no cost for empty ending (our goal: dp[0])
    dp[n] = 0 
    
    # Additional data structure to track where to place line breaks
    breaks = [-1] * n
    
    # Populate DP table, from right to left (back to front)
    for i in range(n-1, -1, -1):
        # try placing line break after word j
        for j in range (i, n): 
            cost = compute_cost(i, j)
            if cost == float('inf'):
                break  # No valid line break if cost is inifinity
            if cost + dp[j+1] < dp[i]:
                dp[i] = cost + dp[j+1]
                breaks[i] = j # Store the optimal end index for line starting at i
                
    # Optional: reconstruct justified text using the breaks array
    res = []
    i = 0
    while i < n:
        j = breaks[i]
        line = ' '.join(words[i:j+1])
        line += ' ' * (max_width - len(line)) # left-justify the line
        res.append(line)
        i = j + 1
    return dp[0], res

# Example usage:
words = ["This", "is", "an", "example", "of", "text", "justification", "using", "dynamic", "programming."]
max_width = 16
min_cost, justified_text = text_justification(words, max_width)
print("The minimum cost of justifying the text: ", min_cost)
for line in justified_text:
    print(f"{line}")