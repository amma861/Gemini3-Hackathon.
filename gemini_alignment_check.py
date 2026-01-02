def calculate_alignment_score(original_text, back_translated_text):
    """
    Simulates a statistical comparison between 
    original intent and the AI's translation.
    """
    orig_set = set(original_text.lower().split())
    back_set = set(back_translated_text.lower().split())
    
    # Calculate Jaccard Similarity (a statistical measure of overlap)
    intersection = orig_set.intersection(back_set)
    union = orig_set.union(back_set)
    
    score = (len(intersection) / len(union)) * 100
    return round(score, 2)

# Example logic
original = "The contract is legally binding in the state of Enugu."
back_translated = "The agreement is binding by law in Enugu state."

print(f"Alignment Score: {calculate_alignment_score(original, back_translated)}%")
