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
            for i in range(max_width - curr_line_length):
                curr_line[i % (len(curr_line) - 1 or 1)] += ' '
            
            # Join words to form the justified line and add to result
            result.append(''.join(curr_line))
            curr_line, curr_line_length = [], 0
            
        # Add the word to the current line
        curr_line.append(word)
        curr_line_length += len(word)
        
    # Handle the last line separately:
    result.append(''.join(curr_line).ljust(max_width))
    return result
        
# Example usage:
words = ["This", "is", "an", "example", "of", "text", "justification."]
max_width = 16
justified_text = full_justify(words, max_width)
for line in justified_text:
    print(f"{line}")
