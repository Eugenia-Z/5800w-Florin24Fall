def full_justify(words, max_width):
    # init variables
    result  = []
    curr_line_length = 0
    curr_line = []
    
    # traver each word in words, whenever adding this word exceeds max_width, process the current words in the list (split into spaces and join) and then res all the line-variables to track the words on the next line
    for word in words:
        if len(curr_line) + len(word) + curr_line_length > max_width:
            # here the trick is using len(curr_line) to gauge the number of spaces as if we already padded
            # if cannot add more word to this line, start process it
            
            # To distribute spaces for the current line, we actually need a bit iteration (test and learn) to find out 
            # there is a total of (max_width-curr_line_length) much of the space to distribute.
            # each iteration essentially just distribute one space only
            # But by using the modulo operation, we're actually able to do it in a cyclic manner.
            # As always the best way to understand the code is to dry run! 
            for i in range(max_width - curr_line_length):
                # rotates the additional spaces across the gaps between words. 
                # by cycling through the gaps, the code distributes extra space as evenly as possible from left to right.
                curr_line[i % max(len(curr_line) - 1,1)] += ' '
            
            # Join words to form the justified line and add to result
            result.append(''.join(curr_line))
            curr_line, curr_line_length = [], 0
            
        # Add the word to the current line
        curr_line.append(word)
        curr_line_length += len(word)
        
    # Handle the last line separately:
    # Here the join actually uses a ' ' space. 
    result.append(' '.join(curr_line).ljust(max_width))
    return result
        
# Example usage:
words = ["This", "is", "an", "example", "of", "text", "justification."]
max_width = 16
justified_text = full_justify(words, max_width)
for line in justified_text:
    print(f"{line}")
