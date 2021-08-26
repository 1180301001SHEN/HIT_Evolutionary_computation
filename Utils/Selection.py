''' @ auther Sr+'''
from TSPproblem.Population import Population
from TSPproblem.Individual import Individual
import random
import copy
from Utils.Crossover import Crossover
import numpy as np

'''elitism selection is not just a selection method, but should use together with other method,
so here we do not implement this algorithm'''


class Selection():
    '''Some methods of selection'''

    def fitness_proportional(population):
        '''fitness_proportional:
        the probability of an individual being selected is proportional to the value of its fitness function'''
        dimension = population.get_dimension()
        individuals = population.get_individuals()
        individual_number = population.get_individual_num()
        dist_mat = population.get_dist_mat()
        individuals_child = list()
        individuals_now_size = len(individuals)

        fitness = list()
        sum = 0
        for i in range(individuals_now_size):
            fit_score = 1/individuals[i].compute_total_distance(dist_mat)
            fitness.append(fit_score)
            sum += fit_score
        fitness = fitness/sum
        end = list()
        sum = 0
        for i in range(individuals_now_size):
            sum += fitness[i]
            end.append(sum)
        for i in range(individual_number):
            random_num = random.random()
            for j in range(individuals_now_size):
                if end[j] >= random_num:
                    gene_order = individuals[j].get_gene_order()
                    individual = Individual(dimension)
                    individual.set_gene_order(gene_order)
                    individuals_child.append(individual)
                    break
        population_child = Population(individual_number, dimension, dist_mat)
        population_child.set_individuals(copy.deepcopy(individuals_child))
        return population_child


    def tournament_selection(population, sample_num):
        '''tournament_selection:
        ramdomly choose sample_num individuals of each episode,
        we run individual_number episodes to select individual_number individuals'''
        dimension = population.get_dimension()
        individuals = population.get_individuals()
        individual_number = population.get_individual_num()
        dist_mat = population.get_dist_mat()
        individuals_child = list()

        individuals_now_size = len(individuals)

        for i in range(individual_number):
            candidates = list()
            candidates_list = np.random.choice(
                individuals_now_size, sample_num, replace=False)
            for i in candidates_list:
                candidates.append(individuals[i])
            best_score = candidates[0].compute_total_distance(dist_mat)
            best_gene = candidates[0].get_gene_order()
            for candidate in candidates:
                temp_score = candidate.compute_total_distance(dist_mat)
                if temp_score < best_score:
                    best_score = temp_score
                    best_gene = candidate.get_gene_order()
            individual = Individual(dimension)
            individual.set_gene_order(best_gene)
            individuals_child.append(individual)
        population_child = Population(individual_number, dimension, dist_mat)
        population_child.set_individuals(copy.deepcopy(individuals_child))
        return population_child


if __name__ == "__main__":
    dist_mat = [[0, 1, 10, 3], [1, 0, 2, 3], [10, 2, 0, 4], [3, 3, 4, 0]]
    individual_num = 4
    dimension = 4
    population = Population(individual_num, dimension, dist_mat)
    individual_list = population.get_individuals()
    print(len(individual_list))
    new_gen = list()
    for i in range(0, individual_num-1, 2):
        individual1 = copy.deepcopy(individual_list[i])
        individual2 = copy.deepcopy(individual_list[i+1])

        new_individual1, new_individual2 = Crossover.Order_Crossover(
            individual1, individual2)
        individual_list.append(new_individual1)
        individual_list.append(new_individual2)
    print(len(individual_list))
    population.set_individuals(copy.deepcopy(individual_list))
    print(len(population.get_individuals()))
    population_child = Selection.tournament_selection(population, 3)
    print(len(population_child.get_individuals()))
