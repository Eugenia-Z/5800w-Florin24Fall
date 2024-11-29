def lcs(X, Y):
    V = {}  # init to dict
    for i in range(len(X) + 1): 
        V[(i, 0)] = ""
    for j in range(len(Y) + 1): 
        V[(0, j)] = ""
    
    # Fill in the 2D dp table
    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            if x == y:
                V[(i+1, j+1)] = V[(i,j)] + x
            else:
                V[(i+1, j+1)] = max([V[(i+1, j)],V[(i,j+1)]], key=len)
    return V[(len(X), len(Y))]
print(lcs('xxxxxaxxxbxxc', 'abc'))


# Using dict actually makes it a higher dimension, storing all the actual strings! Impressive! 