import woaWSR as woa
import functions as f
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

max_iter = 100
number_experiments = 100
matrix = np.zeros((max_iter,number_experiments))

for i in range(number_experiments):
    fitness = f.function_schaffer
    dim=2
    num_whales = 50
    rewiring = 0.3
    G = nx.generators.random_graphs.watts_strogatz_graph(num_whales, 3, rewiring)
    
    best_array, best_position = woa.woa(fitness, max_iter, num_whales, dim, -100, 100, G, rewiring)
    matrix[i,:] = best_array
    
average = np.average(matrix, axis=0)
np.save("woawsr", average)
plt.figure(dpi=300)
plt.grid()
plt.xlabel("Average in iterations")
plt.ylabel("Fitness")

plt.plot(average)
plt.yscale("log")
#plt.show()
plt.savefig("woaWSR.png")

for i in range(number_experiments):
    fitness = f.function_eggholder
    dim=2
    num_whales = 50
    rewiring = 0.3
    G = nx.generators.random_graphs.watts_strogatz_graph(num_whales, 3, rewiring)
    
    best_array, best_position = woa.woa(fitness, max_iter, num_whales, dim, -512, 521, G, rewiring)
    matrix[i,:] = best_array
    
average = np.average(matrix, axis=0)
np.save("woawsr2", average)
plt.figure(dpi=300)
plt.grid()
plt.xlabel("Average in iterations")
plt.ylabel("Fitness")

plt.plot(average)
#plt.show()
plt.savefig("woa2WSR.png")