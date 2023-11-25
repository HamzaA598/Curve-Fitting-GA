# inputs: population size, chromosome length
# output: (list/2d numpy array) of numpy arrays where each inner array is
# a chromosome (coeffieicents)
def initalize():
    pass

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