import numpy as np


class GeneticEquation:

    def __init__(self, equation, rate, pop_size=100):
        self.population = np.random.uniform(size=pop_size) * 10
        self.equation = equation
        self.rate = rate

    def sort_by_fitness(self):
        fitness = np.array([abs(self.equation(i)) for i in self.population])
        self.population = self.population[fitness.argsort()]

    def cross(self):
        for i in range(10, 99):
            parents = self.population[np.random.randint(0, 99, 2)]
            floating_part = str(parents[1] - int(parents[1]))[1:]
            int_part_1 = int(parents[0])
            int_part_2 = int(parents[1])

            bin_part_1 = '{0:08b}'.format(int_part_1)
            bin_part_2 = '{0:08b}'.format(int_part_2)

            if (i * np.random.random()) > self.rate:
                cross_point = np.random.randint(0, 8)
                binary_number = bin_part_1[:cross_point] + bin_part_2[cross_point:]
                float_number = str(int(binary_number, 2)) + floating_part
                self.population[i] = float(float_number)
            else:
                self.population[i] = parents[0]

    def mutate(self):
        for i in range(10, 100):
            if np.random.random() < self.rate:
                self.population[i] = np.random.random() * 10

    def find_root(self):
        for i in range(100):
            self.sort_by_fitness()
            self.cross()
            self.mutate()

        print(f'Root is {self.population[0]}')


eq = lambda x: 9 * (x) ** 5 - 194.7 * (x) ** 4 + 1680.1 * (x) ** 3 - 7227.94 * (x) ** 2 + 15501.2 * (x) - 13257.2

root_finder = GeneticEquation(equation=eq, rate=0.6, pop_size=100)
root_finder.find_root()
