import numpy as np
import math
import random

def function_eggholder(position):
	# X is a np.array
	return (-(position[1] + 47) * np.sin(np.sqrt(abs(position[0]/2 + (position[1] + 47)))) -position[0] * np.sin(np.sqrt(abs(position[0] - (position[1] + 47)))))

# schaffer function 4
def function_schaffer(position):
    top = math.pow(math.sin(math.pow(position[0],2) - math.pow(position[1],2)),2)- 0.5
    button = math.pow(1+(0.0001*(math.pow(math.pow(position[0],2) + math.pow(position[1],2),2))),2)
    return 0.5 + (top/button)

# schaffer function 4
def function_matyas(position):
    first = math.pow(position[0],2) + math.pow(position[1],2)
    second = 0.26*first- (0.48*position[0]*position[1])
    return second

def qap_cost(chromosome, distances, flows):
    """Gets the fitness score for a particular chromosome using the formula minϕ∈Sn ∑ni=1 ∑nj=1 fij⋅dϕ(i)ϕ(j)
    Parameters
    ----------
    chromsome : list
        list of values
    distances : list
        list of distance mapping for each data in the population
    flows : list
        list of flow mappings for each data in the population
    Returns
    -------
    int
        return cost for particular chromosome
    """
    searched_list = []
    cost = 0
    
    for j in chromosome:
            for k in chromosome:

                # since problem is a 1-1 type, mapping (1,2) == (2,1).
                if (k, j) in searched_list or (j, k) in searched_list: continue

                print("cromosoma",chromosome, j, k)
                
                # cost = cost + flow(f1, f2) * distance(d1, d2) for every f1, f2, d1, d2.
                cost += Get_Distance_Or_Flow(j,k, distances) * Get_Distance_Or_Flow(chromosome[j], chromosome[k], flows)

                # append mapping to searched list to save time.
                searched_list.append((j, k))
    
    return cost

def Get_Distance_Or_Flow(i, j, dictionary) -> int:
    """return distance or flow value based on mapping (i, j)
    Parameters
    ----------
    i : int
        first location/facilty
    j : int
        second location/facility
    dictionary : dict
        dicttionary to search
    Returns
    -------
    int
        integer value from dictionary based on mapping (i, j)
    """
    print(dictionary)
    if (i, j) not in dictionary:
        print(i,j)
        return dictionary[j, i]
    
    return dictionary[i, j]

def Generate_Distance_Or_Flow(size, upper_bound) -> dict:
    """Generate random values for distance and flows between location and facilities
    Parameters
    ----------
    size : int
        The length of location/facility
    value_range : int
        The upper bound for the value of distance/flow
    Returns
    -------
    dictionary
        a dictionary where key == tuple of location/facility mapping and value == integer value of distance/flow for 
        that mapping
    """

    dictionary = {}
    for i in range(size):
        for j in range(size):
            
            if i == j: dictionary[i,j] = 0

            # since problem is a one-one problem, mapping (1,2) == (2,1) so there's no need to create duplicate mappings
            if (j,i) in dictionary: continue
            
            dictionary[i,j] = random.randrange(0, upper_bound)

    return dictionary