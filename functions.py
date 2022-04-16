import numpy as np
import math
import random

def function_bukin(position):
    # X is a np.array
    x = position[0]
    y = position[1]
    if x >= -15 and x <= -5 and y >= -3 and y <= 3:
        return 100*math.sqrt(abs(y-0.01*x**2))+0.01*abs(x+10)
    else:
        return float("inf")
# schaffer function 2
def function_schaffer(position):
    x = position[0]
    y = position[1]
    top = math.pow(math.sin(math.pow(position[0],2) - math.pow(position[1],2)),2)- 0.5
    button = math.pow(1+(0.0001*(math.pow(math.pow(position[0],2) + math.pow(position[1],2),2))),2)
    if x>=-100 and y <= 100:
        return 0.5 + (top/button)
    else:
        return float("inf")

# function_matyas function
def function_matyas(position):
    x = position[0]
    y = position[1]
    first = math.pow(position[0],2) + math.pow(position[1],2)
    second = 0.26*first- (0.48*position[0]*position[1])
    if x>= -10 and y <= 10:
        return second
    else:
        return float("inf")

#Three-hump camel function function
def function_three_hump(position):
    x = position[0]
    y = position[1]
    if x>=-5 and y<=5:
        return 2*x**2-1.05*x**4+(x**6)/6+x*y+y**2
    else:
        return float("inf")

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