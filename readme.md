#### Requirements:
(1)Python3
(2)numpy
(3)random
(4)copy
(5)math

All outputs are stored in './log/' and we just store once per 5000 iterations.

You may just run the 'Experiment/experiment1.py' or 'Experiment/experiment2.py', but if it doesn't work, please just change the file path, and it would run successfully.

The file named pr2392 is too long to run, and when the population is 100, it takes us nearly 72h to run the entire 20000 iteration of sga1. So, we do not run the sga2 and sga3 on the pr2392 which population is 100.

**The location of files**
The class TSPProblem of Exercise 1 is implemented in ./TSPproblem/TSPproblem.py.
The class Individual of Exercise 2 is implemented in ./TSPproblem/Individual.py.
The class Population of Exercise 2 is implemented in ./TSPproblem/Population.py.
The different mutation operators of Exercise 3 are implemented in ./TSPproblem/Individual.py.
The different crossover operators of Exercise 3 are implemented in ./Utils/Crossover.py.
The different selection methods of Exercise 4 are implemented in ./Utils/Selection.py.
Three different evolutionary algorithms using crossover and mutation, based on the implementation of our different modules are implemented in ./Experiment/sga.py.
The results of the two experiments are sorted out and stored in ./log