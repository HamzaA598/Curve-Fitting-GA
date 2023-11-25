import numpy as np
import random
import math

POP_SIZE = 8
K = math.ceil(0.2*POP_SIZE)
LOWER_BOUND = -10
UPPER_BOUND = 10
Pc = 0.7
Pm = 0.01

# utility functions used for calculating fitness value of chromosome
def mean_square_error(chromosome, x, y):
    predicted_values = evaluate_polynomial(chromosome, x)
    squared_errors = (predicted_values - y) ** 2
    mse = np.mean(squared_errors)
    return mse

def evaluate_polynomial(chromosome, x):
    return np.polyval(chromosome, x)


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


# inputs: population, fitness_values, size of tournament?
# output: selected parents
def select(population, fitness_values, tournament_size=2):
    selection_size = POP_SIZE - K
    selected_parents = np.empty([selection_size, population.shape[1]])
    for i in range(selection_size):
        tournament_indices = np.random.choice(POP_SIZE, size=tournament_size, replace=True)
        
        # this line is equivalent to
        # tournament_fitness = [fitness_values[i] for i in tournament_indices]
        # where it gets the fitness values for the indices selected for tournament
        tournament_fitness = fitness_values[tournament_indices]

        winner_index = tournament_indices[np.argmax(tournament_fitness)]
        selected_parents[i] = population[winner_index]
    return selected_parents

# inputs: selected parents
# output: intermediate generation of parents and children
def crossover():
    pass

# inputs: intermediate generation of parents and children
# output: mutated generation
def mutate(intermediate_population, t, T):
    # dependency factor
    b = 1

    for chromosome in intermediate_population:
        for gene in chromosome:
            Pmi = random.random()
            if Pmi > Pm:
                continue

            r1 = random.random()
            #calculating delta
            y = gene - LOWER_BOUND if r1 <= 0.5 else UPPER_BOUND - gene
            r2 = random.random()
            delta_t_y = y*(1-r2**((1-t/T)**b))
            gene = gene - delta_t_y if r1 <= 0.5 else gene + delta_t_y
            
    return intermediate_population


# inputs: mutated generation, old generation and their fitness_values
# output: new population with elitism replacment
# combines the elite members with the offspring
def replace():
    pass
