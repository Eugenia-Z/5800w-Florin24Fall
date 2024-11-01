def GiveChange(C, S):
    # Create list to store answers to subproblems
    V = [float('inf')] * (S+1)
    V[0] = 0
    for i in range(S+1):
        for c in C:
            if c <= i:
                V[i] = min(V[i], V[i-c]+1)
    return V[S]

if __name__ == "__main__":
    print(GiveChange([1,5,10,21,25], 63))