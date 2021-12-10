import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from newWOAWSR import jfs   # change this to switch algorithm 
import matplotlib.pyplot as plt

# load data
data  = pd.read_csv('ionosphere.csv')
data  = data.values
feat  = np.asarray(data[:, 0:-1])
label = np.asarray(data[:, -1])

# split data into train & validation (70 -- 30)
xtrain, xtest, ytrain, ytest = train_test_split(feat, label, test_size=0.3, stratify=label)
fold = {'xt':xtrain, 'yt':ytrain, 'xv':xtest, 'yv':ytest}


# parameter
k                   = 5     # k-value in KNN
N                   = 20    # number of whales
T                   = 100   # maximum number of iterations
number_experiments  = 10
opts = {'k':k, 'fold':fold, 'N':N, 'T':T}

matrix = np.zeros((number_experiments,T))
average_acc = []

# perform feature selection
for i in range(number_experiments):
    fmdl = jfs(feat, label, opts)
    sf   = fmdl['sf']
    
    # model with selected features
    num_train = np.size(xtrain, 0)
    num_valid = np.size(xtest, 0)
    x_train   = xtrain[:, sf]
    y_train   = ytrain.reshape(num_train)  # Solve bug
    x_valid   = xtest[:, sf]
    y_valid   = ytest.reshape(num_valid)  # Solve bug
    
    mdl       = KNeighborsClassifier(n_neighbors = k) 
    mdl.fit(x_train, y_train)
    
    # accuracy
    y_pred    = mdl.predict(x_valid)
    Acc       = np.sum(y_valid == y_pred)  / num_valid
    curve   = fmdl['c']    
    print(curve.shape)
    matrix[i,:] = curve
    average_acc.append(Acc)
    #print("Accuracy:", 100 * Acc)
    
    # number of selected features
    #num_feat = fmdl['nf']
    #print("Feature Size:", num_feat)

# plot convergence
average_acc = np.array(average_acc)
#print(average_acc)
#print(np.average(average_acc))
#print("matrix", matrix)
average = np.average(matrix, axis=0)
curve   = average
np.save("newWOAWSR", average)
#print(curve)
#curve   = curve.reshape(np.size(curve,1))
#print(curve)
x       = np.arange(0, opts['T'], 1.0) + 1.0

fig, ax = plt.subplots()
ax.plot(x, curve, 'o-')
ax.set_xlabel('Number of Iterations')
ax.set_ylabel('Fitness')
ax.set_title('PSO')
ax.grid()
plt.yscale("log")

#plt.show().savefig("")
plt.savefig("newWOAWSR.png")