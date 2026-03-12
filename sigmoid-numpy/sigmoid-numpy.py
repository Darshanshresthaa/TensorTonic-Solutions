# Write your code 

import numpy as np

def sigmoid(x):

    x = np.array(x)

    if x is not None:
        return 1/(1+np.exp(-x))
    else:
        return None