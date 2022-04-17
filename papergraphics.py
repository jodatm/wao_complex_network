"""
Paper graphics from numpy files
Date: 15-April-2022
"""
import numpy as np
import matplotlib.pyplot as plt

wao_function_schaffer = np.load("schafferWAO.npy")
wao_function_bukin = np.load("bukinWAO.npy")
wao_function_hump = np.load("humpWAO.npy")
wao_function_matyas = np.load("matyasWAO.npy")

wao_watts_strogatz_graph_function_schaffer = np.load("schafferNetwork.npy")
wao_watts_strogatz_graph_function_bukin = np.load("bukinNetwork.npy")
wao_watts_strogatz_graph_function_hump = np.load("humpNetwork.npy")
wao_watts_strogatz_graph_function_matyas = np.load("matyasNetwork.npy")
"""
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
"""

plt.figure(dpi=300)
#plt.title("Comparations functions")
plt.grid()
plt.xlabel("Iteration")
plt.ylabel("Fitness")
plt.plot(wao_function_bukin,'g-',label="Bukin WAO")
plt.plot(wao_watts_strogatz_graph_function_bukin,'g--',label="Bukin small-world graph")
plt.plot(wao_function_schaffer,'b-',label="Schaffer WAO",)
plt.plot(wao_watts_strogatz_graph_function_schaffer,'b--',label="Schaffer small-world graph")
plt.plot(wao_function_hump,'r-',label="Hump WAO")
plt.plot(wao_watts_strogatz_graph_function_hump,'r--',label="Hump small-world graph")
plt.plot(wao_function_matyas,'c-',label="Matyas WAO",)
plt.plot(wao_watts_strogatz_graph_function_matyas,'c--',label="Matyas small-world graph")
plt.yscale("log")
plt.legend()
plt.tight_layout()
plt.savefig("all_functions.png")
