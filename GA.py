import numpy as np

POP_SIZE = 8
K = 0.2*POP_SIZE
LOWER_BOUND = -10
UPPER_BOUND = 10

# inputs: chromosome length
# output: (list/2d numpy array) of numpy arrays where each inner array is
# a chromosome (coeffieicents)
def initialize(chromosome_length):
    initial_population = np.random.uniform(LOWER_BOUND, UPPER_BOUND, size=(POP_SIZE, chromosome_length))
    return initial_population

# inputs: population, data pojnts
# ouput: (list/numpy array) of fitness_values
def fitness(population, x, y):
    fitness_values = np.empty([POP_SIZE, 1])
    for i in range(POP_SIZE):
        chromosome = population[i]
        # Negative so we can maximize the fitness values
        fitness_values[i] = -mean_square_error(chromosome, x, y)
    return fitness_values


def mean_square_error(chromosome, x, y):
    predicted_values = evaluate_polynomial(chromosome, x)
    squared_errors = (predicted_values - y) ** 2
    mse = np.mean(squared_errors)
    return mse


def evaluate_polynomial(chromosome, x):
    return np.polyval(chromosome, x)

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
def mutation(intermediate_population, current_generation_no, max_generations):
    pass

# inputs: mutated generation, old generation and their fitness_values
# output: new population with elitism replacment
def replacment():
    pass
