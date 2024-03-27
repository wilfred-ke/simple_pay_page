import numpy as np

# Define the function to integrate
def f(x):
    return 1 / (1 + np.sqrt(x))

# Define integration limits
a = 1  # Lower limit
b = 4  # Upper limit

# Number of random points to sample
N = 15

# Generate random points in the integration domain
x_values = np.random.uniform(a, b, N)

# Evaluate the function at the sampled points
f_values = f(x_values)

# Calculate the integral estimate
integral_estimate = np.mean(f_values) * (b - a)

# print("Monte Carlo integral estimate:", integral_estimate)
print('\n', x_values)
