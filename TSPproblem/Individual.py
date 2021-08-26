''' @ auther Sr+'''
import random
import copy
import numpy as np


class Individual():
    '''Every individual in the population,
    dimension means the gene size of the individual,
    the gene_order means the gene list of the individual'''

    def __init__(self, dimension) -> None:
        self.dimension = dimension
        self.gene_order = [i for i in range(dimension)]
        random.shuffle(self.gene_order)

    def set_gene_order(self, gene_order):
        '''set the gene list of the individual'''
        self.gene_order = copy.deepcopy(gene_order)

    def compute_total_distance(self, dist_mat):
        '''return the fitness of the individual'''
        self.total_distance = 0.0
        for i in range(self.dimension - 1):
            from_idx = self.gene_order[i]
            to_idx = self.gene_order[i + 1]
            self.total_distance += dist_mat[from_idx][to_idx]
        self.total_distance += dist_mat[self.gene_order[-1]
                                        ][self.gene_order[0]]

        return self.total_distance

    def insert(self):
        '''A method of mutation called insert,
        randomly choose two posotions of the gene list,
        insert one gene in front of the other'''
        self.gene_order = list(self.gene_order)
        x1, x2 = np.random.choice(range(0, self.dimension), 2, replace=False)
        self.gene_order.remove(x2)
        self.gene_order.insert(self.gene_order.index(x1)+1, x2)

    def swap(self):
        '''A method of mutation called swap,
        randomly choose two posotions of the gene list,
        swap them'''
        index1, index2 = np.random.choice(
            range(0, self.dimension), 2, replace=False)
        temp = self.gene_order[index1]
        self.gene_order[index1] = self.gene_order[index2]
        self.gene_order[index2] = temp

    def inversion(self):
        '''A method of mutation called inversion,
        randomly choose two posotions of the gene list,
        invert the sublist between the two position'''
        self.gene_order = list(self.gene_order)
        index1, index2 = np.random.choice(
            range(0, self.dimension), 2, replace=False)
        min_index = min(index1, index2)
        max_index = max(index1, index2)
        sublist = self.gene_order[min_index:max_index+1]
        for iterm in sublist:
            self.gene_order.remove(iterm)
        sublist.reverse()
        for i in range(len(sublist)):
            self.gene_order.insert(min_index+1+i, sublist[i])

    def scramble(self):
        '''A method of mutation called insert,
        randomly choose several posotions of the gene list,
        shuffle the gene on these positions'''
        self.gene_order = list(self.gene_order)
        gene_number_to_change = random.randint(0, self.dimension-1)
        positions = list()
        numbers = list()
        for i in range(gene_number_to_change+1):
            position = random.randint(0, self.dimension-1)
            while position in positions:
                position = random.randint(0, self.dimension-1)
            positions.append(position)
            numbers.append(self.gene_order[position])
        random.shuffle(numbers)
        for i in range(len(numbers)):
            self.gene_order[positions[i]] = numbers[i]

    def get_gene_order(self):
        '''return the gene list of the individual'''
        return copy.deepcopy(self.gene_order)


if __name__ == "__main__":
    individual = Individual(10)
    print(list(individual.get_gene_order()))

    individual.insert()
    print(list(individual.get_gene_order()))

    individual.inversion()
    print(list(individual.get_gene_order()))

    individual.swap()
    print(list(individual.get_gene_order()))

    individual.scramble()
    print(list(individual.get_gene_order()))
