import woa as woa
import woaWS as woaG
import numpy as np
import matplotlib.pyplot as plt
import functions as f
import networkx as nx

def experiments_wao(f,filename,max_iter,number_experiments,num_whales,dim):
    matrix = np.zeros((max_iter,number_experiments))

    for i in range(number_experiments):
        fitness = f
      
        best_array, best_position = woa.woa(fitness, max_iter, num_whales, dim, -100, 100)
        matrix[i,:] = best_array
        
    average = np.average(matrix, axis=0)
    np.save(filename, average)
    plt.figure(dpi=300)
    plt.grid()
    plt.xlabel("Average in iterations")
    plt.ylabel("Fitness")

    plt.plot(average)
    plt.yscale("log")
    #plt.show()
    plt.savefig(filename+".png")

def experiments_network(f,filename,max_iter,number_experiments,num_whales,dim,rewiring):
    matrix = np.zeros((max_iter,number_experiments))
    for i in range(number_experiments):
        fitness = f
        G = nx.generators.random_graphs.watts_strogatz_graph(num_whales, 3, rewiring)
        
        best_array, best_position = woaG.woa(fitness, max_iter, num_whales, dim, -100, 100, G)
        matrix[i,:] = best_array
        
    average = np.average(matrix, axis=0)
    np.save(filename, average)
    plt.figure(dpi=300)
    plt.grid()
    plt.xlabel("Average in iterations")
    plt.ylabel("Fitness")

    plt.plot(average)
    plt.yscale("log")
    #plt.show()
    plt.savefig(filename+".png")

max_iter = 100
number_experiments = 100
num_whales = 100
dim = 2
rewiring = 0.3
experiments_wao(f.function_bukin,"bukinWAO",max_iter,number_experiments,num_whales, dim)
experiments_network(f.function_bukin,"bukinNetwork",max_iter,number_experiments,num_whales, dim,rewiring)

experiments_wao(f.function_levi,"leviWAO",max_iter,number_experiments,num_whales, dim)
experiments_network(f.function_levi,"leviNetwork",max_iter,number_experiments,num_whales, dim,rewiring)

experiments_wao(f.function_matyas,"matyasWAO",max_iter,number_experiments,num_whales,dim)
experiments_network(f.function_matyas,"matyasNetwork",max_iter,number_experiments,num_whales, dim,rewiring)


experiments_wao(f.function_schaffer,"schafferWAO",max_iter,number_experiments,num_whales, dim)
experiments_network(f.function_schaffer,"schafferNetwork",max_iter,number_experiments,num_whales, dim,rewiring)