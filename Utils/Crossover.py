''' @ auther Sr+'''
import random
from TSPproblem.Individual import Individual
import numpy as np
import copy
from Utils.edge import edge_element, edge_table


class Crossover():
    '''Some crossover methods'''

    def Order_Crossover(individual1, individual2):
        '''Order_Crossover:
        ramdomly get a sublist of the gene of one individual,
        and put the other sublist relative position unchanged'''
        gene_order1 = np.array(individual1.get_gene_order())
        gene_order2 = np.array(individual2.get_gene_order())

        gene_order1_new = copy.deepcopy(gene_order1)
        gene_order2_new = copy.deepcopy(gene_order2)

        length = len(gene_order1)
        from_index, to_index = np.random.choice(length, 2, replace=False)
        min_from_to, max_from_to = min(
            [from_index, to_index]), max([from_index, to_index])
        r_from_to = range(min_from_to, max_from_to+1)
        r_left = np.delete(range(length), r_from_to)

        middle_1, middle_2 = gene_order1[r_from_to], gene_order2[r_from_to]

        gene_order1_new[r_from_to] = middle_1
        gene_order2_new[r_from_to] = middle_2

        j = 0
        k = 0
        for i in range(length):
            if gene_order2[i] not in middle_1 and j < len(r_left):
                gene_order1_new[r_left[j]] = gene_order2[i]
                j += 1
            if gene_order1[i] not in middle_2 and k < len(r_left):
                gene_order2_new[r_left[k]] = gene_order1[i]
                k += 1

        new_individual1 = Individual(length)
        new_individual1.set_gene_order(gene_order1_new)
        new_individual2 = Individual(length)
        new_individual2.set_gene_order(gene_order2_new)

        return new_individual1, new_individual2

    def PMX_Crossover(individual1, individual2):
        '''PMX_Crossover:
        ramdomly get a sublist of the gene of one individual,
        we obtain the corresponding relation of relative position,
        then form the whole new individual'''
        gene_order1 = np.array(individual1.get_gene_order())
        gene_order2 = np.array(individual2.get_gene_order())

        length = len(gene_order1)

        from_index, to_index = np.random.choice(length, 2, replace=False)
        min_from_to, max_from_to = min(
            [from_index, to_index]), max([from_index, to_index])
        r_from_to = range(min_from_to, max_from_to)

        r_left = np.delete(range(length), r_from_to)

        left_1, left_2 = gene_order1[r_left], gene_order2[r_left]
        middle_1, middle_2 = gene_order1[r_from_to], gene_order2[r_from_to]
        gene_order1[r_from_to], gene_order2[r_from_to] = middle_2, middle_1
        mapping = [[], []]
        for i, j in zip(middle_1, middle_2):
            if j in middle_1 and i not in middle_2:
                index = np.argwhere(middle_1 == j)[0, 0]
                value = middle_2[index]
                while True:
                    if value in middle_1:
                        index = np.argwhere(middle_1 == value)[0, 0]
                        value = middle_2[index]
                    else:
                        break
                mapping[0].append(i)
                mapping[1].append(value)
            elif i in middle_2:
                pass
            else:
                mapping[0].append(i)
                mapping[1].append(j)
        for i, j in zip(mapping[0], mapping[1]):
            if i in left_1:
                left_1[np.argwhere(left_1 == i)[0, 0]] = j
            elif i in left_2:
                left_2[np.argwhere(left_2 == i)[0, 0]] = j
            if j in left_1:
                left_1[np.argwhere(left_1 == j)[0, 0]] = i
            elif j in left_2:
                left_2[np.argwhere(left_2 == j)[0, 0]] = i
        gene_order1[r_left], gene_order2[r_left] = left_1, left_2

        new_individual1 = Individual(length)
        new_individual1.set_gene_order(gene_order1)
        new_individual2 = Individual(length)
        new_individual2.set_gene_order(gene_order2)

        return new_individual1, new_individual2

    def Cycle_Crossover(individual1, individual2):
        '''Cycle_Crossover:
        use the corresponding relation of relative position to form a cycle,
        then fill the other position'''
        gene_order1 = list(individual1.get_gene_order())
        gene_order2 = list(individual2.get_gene_order())

        gene_order1_new = copy.deepcopy(gene_order1)
        gene_order2_new = copy.deepcopy(gene_order2)

        length = len(gene_order1)

        begin_index = random.randint(0, length-1)
        index_list = list()
        index_list.append(begin_index)
        begin__num = gene_order1[begin_index]
        next_index = begin_index

        while True:
            if len(index_list) == length:
                break
            next_num = gene_order2[next_index]
            if next_num == begin__num:
                break
            next_index = gene_order1.index(next_num)
            index_list.append(next_index)
        gene_order1 = np.array(gene_order1)
        gene_order2 = np.array(gene_order2)

        gene_order1_new = np.array(gene_order1_new)
        gene_order2_new = np.array(gene_order2_new)

        r_left = np.delete(range(length), index_list)
        gene_order1_new[r_left] = gene_order2[r_left]
        gene_order2_new[r_left] = gene_order1[r_left]

        new_individual1 = Individual(length)
        new_individual1.set_gene_order(gene_order1_new)
        new_individual2 = Individual(length)
        new_individual2.set_gene_order(gene_order2_new)
        return new_individual1, new_individual2

    def Edge_Recombination(individual1, individual2):
        '''Edge_Recombination:
        use the gene of parent individual 
        and fill in the table which means the gene adjacency,
        then randomly choose a row and choose its next using the least adjacency'''
        gene_order1 = list(individual1.get_gene_order())
        gene_order2 = list(individual2.get_gene_order())
        length = len(gene_order1)

        table = edge_table(length)
        for i in range(length):
            row = table.get_row(i)
            index1 = gene_order1.index(i)
            index2 = gene_order2.index(i)
            element_numbers = [-1] * 4

            element_numbers[0] = gene_order1[length -
                                             1 if index1-1 == -1 else index1-1]
            element_numbers[1] = gene_order1[0 if index1 +
                                             1 == length else index1+1]
            element_numbers[2] = gene_order2[length -
                                             1 if index2-1 == -1 else index2-1]
            element_numbers[3] = gene_order2[0 if index2 +
                                             1 == length else index2+1]

            for element_number in element_numbers:
                element = row.get_element(element_number)
                if element is not None:
                    element.set_common(True)
                else:
                    row.get_elements().append(
                        edge_element(element_number, False))
        # table.show()
        start = random.randint(0, length-1)
        gene_order1_new = list()
        while len(gene_order1_new) < length:
            gene_order1_new.append(start)

            candidates = table.get_row(start).get_elements()
            if len(candidates) == 0:
                break
            table.delete_number(start)
            length_map = dict()
            for candidate in candidates:
                index = candidate.get_number()
                row_list = table.get_row(index).get_elements()
                length_map[index] = len(row_list)
            min_key = length
            min_value = length
            for key, value in length_map.items():
                if value < min_value:
                    min_value = value
                    min_key = key
            start = min_key
        new_individual1 = Individual(length)
        new_individual1.set_gene_order(gene_order1_new)

        return new_individual1


if __name__ == "__main__":
    individual1 = Individual(10)
    print(list(individual1.get_gene_order()))
    individual2 = Individual(10)
    print(list(individual2.get_gene_order()))
    individual1_new, individual2_new = Crossover.Edge_Recombination(
        individual1, individual2)

    print(list(individual1_new.get_gene_order()))
    print(list(individual2_new.get_gene_order()))
