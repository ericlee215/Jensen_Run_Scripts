import numpy as np
#from Tester import rotation_matrix as rm


def reorder(nturbines):
    
    
    x = nturbines[:,1]
    
    ind = np.argsort(x)
    
    myorder = ind
    nturbines = [nturbines[i] for i in myorder]
    nturbines = nturbines[::-1]
    nturbines = np.asarray(nturbines)

    return nturbines