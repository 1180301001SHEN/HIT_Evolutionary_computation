''' @ auther Sr+'''
from Utils.Selection import Selection
import copy
from Utils.Crossover import Crossover
from TSPproblem.Population import Population
from Utils.ConfigReader import ConfigReader
from TSPproblem.TSPProblem import TSPProblem
import random


# sga (3):变异(4)，组合(3)，杂交(3)，选择(3)
# 开始：初始化一个种群population,
# for 里面有n个居民individual,n个居民先变异,杂交(总数量会大于n),选择(保持总数量是n)

class sga():
    def sga1(file_path, population_size, generations_num, posibility_cross, posibility_mutation, sample_num):
        '''mutation method:scramble,
        crossover method:Order_Crossover,
        selection method:tournament_selection'''
        file_name1 = file_path.split("/")[1].split(".")[0]
        file_name = "output/sga1" + "_"+str(file_name1) + \
            "_" + str(population_size) + ".sga"
        f = open(file_name, "w")
        f.write("file_path:"+str(file_path)+"\n")
        f.write("population_size:"+str(population_size)+"\n")
        f.write("generations_num:"+str(generations_num)+"\n")
        f.write("posibility_cross:"+str(posibility_cross)+"\n")
        f.write("posibility_mutation:"+str(posibility_mutation)+"\n")
        f.write("sample_num:"+str(sample_num)+"\n")
        configi = ConfigReader(file_path)
        name, dimension, edge_weight_type, dist_mat = configi.get_all()

        tsp = TSPProblem(name, dimension, edge_weight_type, dist_mat)

        population = Population(population_size, dimension, dist_mat)

        for i in range(generations_num):
            individual_list = population.get_individuals()
            for j in range(population_size):
                probilitym = random.random()
                if probilitym < posibility_mutation:
                    population.individuals[j].scramble()
            for j in range(0, population_size, 2):
                probilityc = random.random()
                if probilityc < posibility_cross:
                    individual1 = copy.deepcopy(individual_list[j])
                    individual2 = copy.deepcopy(individual_list[j+1])

                    new_individual1, new_individual2 = Crossover.Order_Crossover(
                        individual1, individual2)
                    individual_list.append(new_individual1)
                    individual_list.append(new_individual2)
                else:
                    new_individual1 = copy.deepcopy(individual_list[j])
                    new_individual2 = copy.deepcopy(individual_list[j+1])
                    individual_list.append(new_individual1)
                    individual_list.append(new_individual2)

            population.set_individuals(copy.deepcopy(individual_list))
            population = Selection.tournament_selection(population, sample_num)
            if i % 5000 == 0:
                best_gene, best_score = population.get_best()
                f.write("i:"+str(i)+"\n")
                f.write("best_gene:"+str(best_gene)+"\n")
                f.write("best_score:"+str(best_score)+"\n")
            if i % 100 == 0:
                print("i:"+str(i))
                print("best_gene:"+str(best_gene))
                print("best_score:"+str(best_score))
        f.close()

    def sga2(file_path, population_size, generations_num, posibility_cross, posibility_mutation, sample_num):
        '''mutation method:inversion,
        crossover method:PMX_Crossover,
        selection method:tournament_selection'''
        file_name1 = file_path.split("/")[1].split(".")[0]
        file_name = "output/sga2" + "_"+str(file_name1) + \
            "_" + str(population_size) + ".sga"
        f = open(file_name, "w")
        f.write("file_path:"+str(file_path)+"\n")
        f.write("population_size:"+str(population_size)+"\n")
        f.write("generations_num:"+str(generations_num)+"\n")
        f.write("posibility_cross:"+str(posibility_cross)+"\n")
        f.write("posibility_mutation:"+str(posibility_mutation)+"\n")
        f.write("sample_num:"+str(sample_num)+"\n")
        configi = ConfigReader(file_path)
        name, dimension, edge_weight_type, dist_mat = configi.get_all()

        tsp = TSPProblem(name, dimension, edge_weight_type, dist_mat)

        population = Population(population_size, dimension, dist_mat)

        for i in range(generations_num):
            individual_list = population.get_individuals()
            for j in range(population_size):
                probilitym = random.random()
                if probilitym < posibility_mutation:
                    population.individuals[j].inversion()
            for j in range(0, population_size, 2):
                probilityc = random.random()
                if probilityc < posibility_cross:
                    individual1 = copy.deepcopy(individual_list[j])
                    individual2 = copy.deepcopy(individual_list[j+1])

                    new_individual1, new_individual2 = Crossover.PMX_Crossover(
                        individual1, individual2)
                    individual_list.append(new_individual1)
                    individual_list.append(new_individual2)
                else:
                    new_individual1 = copy.deepcopy(individual_list[j])
                    new_individual2 = copy.deepcopy(individual_list[j+1])
                    individual_list.append(new_individual1)
                    individual_list.append(new_individual2)

            population.set_individuals(copy.deepcopy(individual_list))
            population = Selection.tournament_selection(population, sample_num)
            if i % 5000 == 0:
                best_gene, best_score = population.get_best()
                f.write("i:"+str(i)+"\n")
                f.write("best_gene:"+str(best_gene)+"\n")
                f.write("best_score:"+str(best_score)+"\n")
            if i % 100 == 0:
                print("i:"+str(i))
                print("best_gene:"+str(best_gene))
                print("best_score:"+str(best_score))
        f.close()

    def sga3(file_path, population_size, generations_num, posibility_cross, posibility_mutation, sample_num):
        '''mutation method:scramble,
        crossover method:Cycle_Crossover,
        selection method:tournament_selection'''
        file_name1 = file_path.split("/")[1].split(".")[0]
        file_name = "output/sga3" + "_"+str(file_name1) + \
            "_" + str(population_size) + ".sga"
        f = open(file_name, "w")
        f.write("file_path:"+str(file_path)+"\n")
        f.write("population_size:"+str(population_size)+"\n")
        f.write("generations_num:"+str(generations_num)+"\n")
        f.write("posibility_cross:"+str(posibility_cross)+"\n")
        f.write("posibility_mutation:"+str(posibility_mutation)+"\n")
        f.write("sample_num:"+str(sample_num)+"\n")
        configi = ConfigReader(file_path)
        name, dimension, edge_weight_type, dist_mat = configi.get_all()

        tsp = TSPProblem(name, dimension, edge_weight_type, dist_mat)

        population = Population(population_size, dimension, dist_mat)

        for i in range(generations_num):
            individual_list = population.get_individuals()
            for j in range(population_size):
                probilitym = random.random()
                if probilitym < posibility_mutation:
                    population.individuals[j].scramble()
            for j in range(0, population_size, 2):
                probilityc = random.random()
                if probilityc < posibility_cross:
                    individual1 = copy.deepcopy(individual_list[j])
                    individual2 = copy.deepcopy(individual_list[j+1])

                    new_individual1, new_individual2 = Crossover.Cycle_Crossover(
                        individual1, individual2)
                    individual_list.append(new_individual1)
                    individual_list.append(new_individual2)
                else:
                    new_individual1 = copy.deepcopy(individual_list[j])
                    new_individual2 = copy.deepcopy(individual_list[j+1])
                    individual_list.append(new_individual1)
                    individual_list.append(new_individual2)

            population.set_individuals(copy.deepcopy(individual_list))
            population = Selection.tournament_selection(population, sample_num)
            if i % 5000 == 0:
                best_gene, best_score = population.get_best()
                f.write("i:"+str(i)+"\n")
                f.write("best_gene:"+str(best_gene)+"\n")
                f.write("best_score:"+str(best_score)+"\n")
            if i % 100 == 0:
                print("i:"+str(i))
                print("best_gene:"+str(best_gene))
                print("best_score:"+str(best_score))
        f.close()
