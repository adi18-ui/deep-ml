import math
import numpy as np

def softmax(scores):
    max_score = max(scores)

    shifted_scores = [x - max_score for x in scores]
    exp_values = [math.exp(x) for x in shifted_scores]

    exp_sum = sum(exp_values)

    probabilities = [x/exp_sum for x in exp_values]

    return [round(p, 4) for p in probabilities]
scores = [1, 2, 3]
softmax(scores)