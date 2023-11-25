import sys
import numpy as np
from GA import *

MAX_GENERATIONS = 100

def main():
    with open("input.txt", "r") as sys.stdin, \
        open("output.txt", "w") as sys.stdout:
        test_cases = int(input())
        for t in range(test_cases):
            line = input().split()
            n = int(line[0])
            degree = int(line[1])  # length of chromosome

            x = np.empty([n, 1])
            y = np.empty([n, 1])

            for i in range(n):
                line = input().split()
                x[i] = float(line[0])
                y[i] = float(line[1])

            
            population = initialize(degree)
            
            # select random POP_SIZE - K elites
            elite_indices = np.random.choice(POP_SIZE, POP_SIZE - K, replace=False)
            elite = population[elite_indices]
            
            for _ in range(MAX_GENERATIONS):
                fitness_vals = fitness(population, x, y)
                selected_parents = select(population, fitness_vals)
                new_population = crossover(selected_parents)
                mutated_population = mutate(new_population, t + 1, MAX_GENERATIONS)
                population, elite = replace(mutated_population, elite)
            
            fitness_vals = fitness(population, x, y)
            best_index = np.argmax(fitness_vals)
            best_individual = population[best_index]
            mse = -fitness_vals[best_index]
            
            print("dataset index: ", t + 1)
            print(best_individual)
            print("MSE =", mse)


if __name__ == "__main__":
    main()
