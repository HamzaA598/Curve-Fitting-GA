import numpy as np

POP_SIZE = 8
K = 0.2*POP_SIZE

# inputs: chromosome length
# output: (list/2d numpy array) of numpy arrays where each inner array is
# a chromosome (coeffieicents)
def initialize(chromosome_length):

    initial_population = np.empty((POP_SIZE, chromosome_length))
    for i in range(POP_SIZE):
        initial_population[i, :] = np.random.rand(chromosome_length);
    
    return initial_population

# inputs: population, data pojnts
# ouput: (list/numpy array) of fitness_values
def fitness():
    pass

# inputs: population, fitness_values, size of tournament?
# output: selected parents
def selection():
    pass

# inputs: selected parents
# output: intermediate generation of parents and children
def crossover():
    pass

# inputs: intermediate generation of parents and children
# output: mutated generation
def mutation():
    pass

# inputs: mutated generation, old generation and their fitness_values
# output: new population with elitism replacment
def replacment():
    pass
