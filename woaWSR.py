# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 13:49:07 2021

@author: User
"""


# python implementation of whale optimization algorithm (WOA)
# minimizing rastrigin and sphere function


import random
import math  # cos() for Rastrigin
import copy  # array-copying convenience
import sys  # max float
import networkx as nx

# -------fitness functions---------

# rastrigin function


def fitness_rastrigin(position):
    fitness_value = 0.0
    for i in range(len(position)):
        xi = position[i]
        fitness_value += (xi * xi) - (10 * math.cos(2 * math.pi * xi)) + 10
    return fitness_value


def function_schaffer(position):
    top = math.pow(
        math.sin(math.pow(position[0], 2) - math.pow(position[1], 2)), 2) - 0.5
    button = math.pow(
        1+(0.0001*(math.pow(math.pow(position[0], 2) + math.pow(position[1], 2), 2))), 2)
    return 0.5 + (top/button)


# sphere function
def fitness_sphere(position):
    fitness_value = 0.0
    for i in range(len(position)):
        xi = position[i]
        fitness_value += (xi * xi)
    return fitness_value


# -------------------------


# whale class
class whale:
    def __init__(self, fitness, dim, minx, maxx, seed):
        self.rnd = random.Random(seed)
        self.position = [0.0 for i in range(dim)]

        for i in range(dim):
            self.position[i] = ((maxx - minx) * self.rnd.random() + minx)

        self.fitness = fitness(self.position)  # curr fitness


# whale optimization algorithm(WOA)
def woa(fitness, max_iter, n, dim, minx, maxx, network, rewiring):
    rnd = random.Random(0)

    # create n random whales
    whalePopulation = [whale(fitness, dim, minx, maxx, i) for i in range(n)]

    # compute the value of best_position and best_fitness in the whale Population
    Xbest = [0.0 for i in range(dim)]
    Xbest_array = []
    Fbest = sys.float_info.max

    for i in range(n):  # check each whale
        if whalePopulation[i].fitness < Fbest:
            Fbest = whalePopulation[i].fitness
            Xbest = copy.copy(whalePopulation[i].position)

    # main loop of woa
    Iter = 0
    while Iter < max_iter:

        # after every 10 iterations
        # print iteration number and best fitness value so far
        #if Iter % 10 == 0 and Iter > 1:
        #    print("Iter = " + str(Iter) + " best fitness = %.3f" % Fbest)

        # linearly decreased from 2 to 0
        a = 2 * (1 - Iter / max_iter)
        a2 = -1+Iter*((-1)/max_iter)

        for i in range(n):
            A = 2 * a * rnd.random() - a
            C = 2 * rnd.random()
            b = 1
            l = (a2-1)*rnd.random()+1
            p = rnd.random()

            D = [0.0 for i in range(dim)]
            D1 = [0.0 for i in range(dim)]
            Xnew = [0.0 for i in range(dim)]
            Xrand = [0.0 for i in range(dim)]
            if p < 0.5:
                if abs(A) > 1:
                    for j in range(dim):
                        D[j] = abs(C * Xbest[j] -
                                   whalePopulation[i].position[j])
                        Xnew[j] = Xbest[j] - A * D[j]
                else:                    
                    best_n = sys.float_info.max 
                    for k in network[i]:                       
                       if(whalePopulation[k].fitness < best_n):
                           best_n = whalePopulation[k].fitness
                           Xrand = whalePopulation[k].position
                    for j in range(dim):
                            D[j] = abs(C * Xrand[j] - whalePopulation[i].position[j])
                            Xnew[j] = Xrand[j] - A * D[j]
            else:
                for j in range(dim):
                    D1[j] = abs(Xbest[j] - whalePopulation[i].position[j])
                    Xnew[j] = D1[j] * \
                        math.exp(b * l) * math.cos(2 * math.pi * l) + Xbest[j]

            for j in range(dim):
                whalePopulation[i].position[j] = Xnew[j]

        for i in range(n):
            # if Xnew < minx OR Xnew > maxx
            # then clip it
            for j in range(dim):
                whalePopulation[i].position[j] = max(
                    whalePopulation[i].position[j], minx)
                whalePopulation[i].position[j] = min(
                    whalePopulation[i].position[j], maxx)

            whalePopulation[i].fitness = fitness(whalePopulation[i].position)

            if (whalePopulation[i].fitness < Fbest):
                Xbest = copy.copy(whalePopulation[i].position)
                Fbest = whalePopulation[i].fitness

        Iter += 1
        Xbest_array.append(fitness(Xbest))
        for j in range(0, n):            
            edges = network.adj[j]            
            
            neighbors=[]
            for k in edges:                
                neighbors.append(k)                        
            
            for i in range(0,len(neighbors)):
                if random.random() < rewiring:                    
                    random_index = int(random.random()*n)                    
                    network.remove_edge(j, neighbors[i])                    
                    network.add_edge(j,random_index)
    # end-while

    # returning the best solution
    return Xbest_array, Xbest
