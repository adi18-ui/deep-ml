# Implement your function below.
from collections import Counter
def rouge_1_score(reference: str, candidate: str) -> dict:
    """
    Compute ROUGE-1 score between reference and candidate texts.
    
    Returns a dictionary with precision, recall, and f1.
    """
    # Your code here
    reference_words = reference.split()
    candidate_words = candidate.split()

    ref_counter = Counter(reference_words)
    can_counter = Counter(candidate_words)

    overlap_counter = ref_counter & can_counter
    count = sum(overlap_counter.values())

    precision = count / len(candidate_words)
    recall = count / len(reference_words)
    f1 = (2*precision*recall)/(precision + recall)

    d = {'precision': precision, 'recall': recall, 'f1': f1}
    return d


