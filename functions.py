import numpy as np
import math

def function_eggholder(position):
	# X is a np.array
	return (-(position[1] + 47) * np.sin(np.sqrt(abs(position[0]/2 + (position[1] + 47)))) -position[0] * np.sin(np.sqrt(abs(position[0] - (position[1] + 47)))))

# schaffer function 4
def function_schaffer(position):
    top = math.pow(math.sin(math.pow(position[0],2) - math.pow(position[1],2)),2)- 0.5
    button = math.pow(1+(0.0001*(math.pow(math.pow(position[0],2) + math.pow(position[1],2),2))),2)
    return 0.5 + (top/button)