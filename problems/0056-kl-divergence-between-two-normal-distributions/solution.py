import numpy as np
import math
def kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q):
	std_p = sigma_p**2
	std_q = sigma_q**2

	difference = (mu_p - mu_q)**2

	result = (math.log(sigma_q / sigma_p)
    + (std_p + difference) / (2 * std_q)
    - 0.5
)

	return float(result)
