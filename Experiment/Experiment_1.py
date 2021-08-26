''' @ auther Sr+'''
# Run your three algorithms with population sizes 10; 20; 50; 100
# on the instances EIL51, EIL76, EIL101, ST70, KROA100, KROC100, KROD100,
# LIN105, PCB442, PR2392 from TSPlib. Report the outcomes after 5000, 10000,
# and 20000 generations.
import os
import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))
from Experiment.sga import sga


if __name__ == "__main__":
    population_size_list = [10, 20, 50, 100]
    file_path_list = ["ALL_tsp/eil51.tsp", "ALL_tsp/eil76.tsp", "ALL_tsp/eil101.tsp", "ALL_tsp/st70.tsp",
                      "ALL_tsp/kroA100.tsp", "ALL_tsp/kroC100.tsp", "ALL_tsp/kroD100.tsp", "ALL_tsp/lin105.tsp",
                      "ALL_tsp/pcb442.tsp", "ALL_tsp/pr2392.tsp"]
    generations_num_list = [5000, 10000, 20000]
    posibility_cross = 0.9
    posibility_mutation = 0.3
    sample_num = [int(population_size_list[i]/2)
                  for i in range(len(population_size_list))]
    generations_num = 20001

    for i in range(len(file_path_list)):
        for j in range(len(population_size_list)):
            sga.sga1(file_path_list[i], population_size_list[j], generations_num,
                     posibility_cross, posibility_mutation, sample_num[j])
            sga.sga2(file_path_list[i], population_size_list[j], generations_num,
                     posibility_cross, posibility_mutation, sample_num[j])
            sga.sga3(file_path_list[i], population_size_list[j], generations_num,
                     posibility_cross, posibility_mutation, sample_num[j])
