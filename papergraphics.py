"""
Paper graphics from numpy files
Date: 15-April-2022
"""
import numpy as np
import matplotlib.pyplot as plt

woa_function_schaffer = np.load("woa.npy")
woa_function_eggholder = np.load("woa2.npy")
woa_watts_strogatz_graph_function_schaffer = np.load("woawsr.npy")
woa_watts_strogatz_graph_function_eggholder = np.load("woawsr2.npy")

plt.figure(dpi=300)
plt.title("Function Shaffer")

plt.grid()
plt.xlabel("Iteration")
plt.ylabel("Fitness")

plt.plot(woa_function_schaffer,label="WOA")
plt.plot(woa_watts_strogatz_graph_function_schaffer,label="small-world graph")
plt.yscale("log")
plt.legend()
plt.savefig("function_schaffer.png")

plt.figure(dpi=300)
plt.title("Function Eggholder")
plt.grid()
plt.xlabel("Iteration")
plt.ylabel("Fitness")

plt.plot(woa_function_eggholder,label="WOA")
plt.plot(woa_watts_strogatz_graph_function_eggholder,label="small-world graph")
plt.yscale("log")
plt.legend()
plt.savefig("function_eggholder.png")


plt.figure(dpi=300)
plt.title("Comparations functions")
plt.grid()
plt.xlabel("Iteration")
plt.ylabel("Fitness")
plt.plot(woa_function_eggholder,'g-',label="Eggholder WOA")
plt.plot(woa_watts_strogatz_graph_function_eggholder,'b-',label="Eggholder small-world graph")
plt.plot(woa_function_schaffer,'g--',label="Schaffer WOA",)
plt.plot(woa_watts_strogatz_graph_function_schaffer,'b--',label="Schaffer small-world graph")
plt.yscale("log")
plt.legend()
plt.savefig("all_functions.png")
