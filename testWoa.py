import woa as woa
import numpy as np
import matplotlib.pyplot as plt
import functions as f

max_iter = 100
number_experiments = 100
matrix = np.zeros((max_iter,number_experiments))

for i in range(number_experiments):
    fitness = f.function_schaffer
    dim=2
    num_whales = 50
    
    best_array, best_position = woa.woa(fitness, max_iter, num_whales, dim, -100, 100)
    matrix[i,:] = best_array
    
average = np.average(matrix, axis=0)
np.save("woa", average)
plt.figure(dpi=300)
plt.grid()
plt.xlabel("Average in iterations")
plt.ylabel("Fitness")

plt.plot(average)
plt.yscale("log")
#plt.show()
plt.savefig("woa.png")

for i in range(number_experiments):
    fitness = f.function_eggholder
    dim=2
    num_whales = 50
    
    best_array, best_position = woa.woa(fitness, max_iter, num_whales, dim, -512, 512)
    matrix[i,:] = best_array
    
average = np.average(matrix, axis=0)
average = np.abs(-959.6407-average)
np.save("woa2", average)
plt.figure(dpi=300)
plt.grid()
plt.xlabel("Average in iterations")
plt.ylabel("Fitness")

plt.plot(average)
plt.yscale("log")
#plt.show()
plt.savefig("woa2.png")