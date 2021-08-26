''' @ auther Sr+'''
# From these three algorithms, run your best algorithm with a population size of 50 for
# 10000 generations on the ten TSPlib instances mentioned above.
# Report for each instance either (1) the average cost and the standard deviation or
# (2) the median cost and the interquartile range

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
    population_size = 50
    file_path_list = ["ALL_tsp/eil51.tsp", "ALL_tsp/eil76.tsp", "ALL_tsp/eil101.tsp", "ALL_tsp/st70.tsp", "ALL_tsp/kroA100.tsp",
                      "ALL_tsp/kroC100.tsp", "ALL_tsp/kroD100.tsp", "ALL_tsp/lin105.tsp", "ALL_tsp/pcb442.tsp", "ALL_tsp/pr2392.tsp"]
    posibility_cross = 0.9
    posibility_mutation = 0.3
    sample_num = int(population_size/2)
    generations_num = 10001

    for i in range(len(file_path_list)):
        for j in range(10):
            sga.sga2(file_path_list[i], population_size, generations_num,
                    posibility_cross, posibility_mutation, sample_num)
