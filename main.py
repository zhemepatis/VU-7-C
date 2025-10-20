from utils.data_generation import generate_vectors, generate_scalars
from benchmark_functions.sphere import sphere_func
import numpy as np

dimentions = 3
domain = [-5, 5]
set_size = 10

vectors = generate_vectors(dimentions, domain, set_size)
scalars = generate_scalars(vectors, sphere_func)

print(vectors)
print(scalars)