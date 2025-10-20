import numpy as np

# TODO:
# [] choose domain
# [] choose dimention num
# [] generate inp vectors
# [] should data be normalized?

# [] apply neural network
# [] get stats

def sphere_func(vector):
    vector_squared = vector**2
    scalar = np.sum(vector_squared)
    return scalar