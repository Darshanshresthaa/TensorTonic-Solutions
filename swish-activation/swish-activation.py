import numpy as np

def swish(x):
    # Sigmoid Implementation
    x = np.array(x)

    sig = 1/(1+np.exp(-x))

    return  np.array(x * sig)
   