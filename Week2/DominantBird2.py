def find_dominant_species(birds):
    # base case:
    if len(birds) == 1:
        return birds[0]

    # divide
    mid = len(birds) // 2
    L = birds[:mid]
    R = birds[mid:]
    
    # conquer
    dominant_L = find_dominant_species(L)
    dominant_R = find_dominant_species(R)
    
    # combine
    if dominant_L == dominant_R:
        return dominant_L
    else:
        count_L = birds.count(dominant_L) if dominant_L is not None else 0
        count_R = birds.count(dominant_R) if dominant_R is not None else 0
        if count_L > len(birds) // 2:
            return dominant_L
        elif count_R > len(birds) // 2:
            return dominant_R
        else:
            return None

if __name__ == "__main__":
    print(find_dominant_species([3,3,2,1,3,2,3,3,5,2,3]))