def stable_matching(men_preferences, women_preferences):
    # Step1: initialize variables
    n = len(men_preferences)
    free_men = list(men_preferences.keys()) # Men who are not yet matched
    proposals = {man:0 for man in men_preferences} # Track which women each man is proposing to next
    engagements = {} # Track current engagements for women
    
    # Step2: continue until all men are matched
    while free_men:
        man = free_men.pop(0)
        woman = men_preferences[man][proposals[man]] # his next choice
        proposals[man] += 1 # Move to the next preference for the next proposal
        
        if woman not in engagements:
            engagements[woman] = man # Woman is free, they get engaged
        else:
            # Woman is currently engaged, check her preference
            current_partner = engagements[woman]
            if women_preferences[woman].index(man) < women_preferences[woman].index(current_partner):
                # Woman prefers the new man, so she switches to him
                free_men.append(current_partner)  # Her former partner becomes free
                engagements[woman] = man # update her engagement
            else:
                # Woman prefers her current partner, the new man remains free
                free_men.append(man)
                
    # Return the stable matching
    return {woman:man for woman, man in engagements.items()}

# Example preferences
men_preferences = {
    'A': ['X', 'Y', 'Z'],
    'B': ['Y', 'X', 'Z'],
    'C': ['Y', 'Z', 'X']
}

women_preferences = {
    'X': ['B', 'A', 'C'],
    'Y': ['A', 'B', 'C'],
    'Z': ['A', 'B', 'C']
}

# Run the algorithm
stable_pairs = stable_matching(men_preferences, women_preferences)
print("Stable Matching:", stable_pairs)