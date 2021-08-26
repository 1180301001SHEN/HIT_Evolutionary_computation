''' @ auther Sr+'''
from TSPproblem.Individual import Individual
import copy


class Population():
    '''A population contains some individuals, 
    the individual_number means the population should maintain the number after mutation, crossover and selection,
    the dist_mat means the matrix of the distance between the nodes'''

    def __init__(self, individual_number, dimension, dist_mat) -> None:
        self.individual_number = individual_number
        self.dimension = dimension
        self.individuals = [Individual(dimension)
                            for _ in range(self.individual_number)]
        self.dist_mat = dist_mat

    def set_individuals(self, individuals):
        '''set the individual list'''
        self.individuals = copy.deepcopy(individuals)

    def get_best_individual(self):
        '''return the distance of the individual whose distance is the shortest'''
        distance = float("inf")
        for individual in self.individuals:
            temp = individual.compute_total_distance(self.dist_mat)
            print(temp)
            if temp < distance:
                distance = temp
        return distance

    def get_individuals(self):
        '''return the list of the individuals in the population'''
        return self.individuals

    def get_individual_num(self):
        '''return the number of list of the individuals in the population'''
        return self.individual_number

    def get_dist_mat(self):
        '''return the matrix of the node distance'''
        return self.dist_mat

    def get_dimension(self):
        '''return the gene length of the population'''
        return self.dimension

    def get_best(self):
        '''return the smallest fitness and its gene list in the population'''
        best_gene = self.individuals[0].get_gene_order()
        best_score = self.individuals[0].compute_total_distance(self.dist_mat)
        for i in range(self.individual_number):
            temp_score = self.individuals[i].compute_total_distance(
                self.dist_mat)
            if temp_score < best_score:
                best_score = temp_score
                best_gene = self.individuals[i].get_gene_order()
        return best_gene, best_score

    def get_all_individuals(self):
        '''print the individual gene in the population'''
        for individual in self.individuals:
            gene = individual.get_gene_order()
            print(list(gene))


if __name__ == "__main__":
    dist_mat = [[0, 1, 10, 3], [1, 0, 2, 3], [10, 2, 0, 4], [3, 3, 4, 0]]
    poputation = Population(5, 4, dist_mat)
    individuals = poputation.get_individuals()

    for individual in individuals:
        print(list(individual.get_gene_order()))
        individual.inversion()
        print(list(individual.get_gene_order()))

    print(poputation.get_best_individual())
