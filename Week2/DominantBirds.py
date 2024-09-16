def conspecific(S):
    if len(S) == 1:
        return S[0]
    if len(S) == 2:
        if S[0] == S[1]:
            return S[0]
    
    mid = len(S) // 2
    S1 = S[:mid]
    S2 = S[mid:]
    a = conspecific(S1)
    if a is not None and S.count(a) > len(S)//2:
        return a
    else:
        b = conspecific(S2)
        if b is not None and S.count(b) > len(S)//2:
            return b
        else:
            return None
    

if __name__ == "__main__":
    print(conspecific([1,1,2,3,2,2,6,1,5,2,1]))