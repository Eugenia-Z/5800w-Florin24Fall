def GiveChange(C, S):
    # Create list to store answers to subproblems
    V = [float('inf')] * (S+1)
    V[0] = 0  # need a base case
    for i in range(S+1):
        for c in C:
            if c <= i:
                V[i] = min(V[i], V[i-c]+1)
    return V[S]

# Prof Florin's appraoch
def CoinChange(C, S):
    # Create list to store answers to subproblems
    V = [None] * (S+1)
    for i in range(S+1):
        V[i] = i  # initializa to i, assuming using all the '1' coins
        for c in C:
            if c <= i:
                V[i] = min(V[i], V[i-c]+1)
    return V[S]
if __name__ == "__main__":
    print(GiveChange([1,5,10,21,25], 63))