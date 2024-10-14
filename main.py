import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    A = 5
    Z = 10
    r = np.zeros([A, Z])
    for a in range(1, A+1):
        
        aux = [(1/z**a) for z in range(1, Z+1)]
        for z in range(1, Z+1):
            r[a-1, z-1] = (1/z**a) / np.sum(aux)
    
        plt.semilogy(r[a-1, :], label=str(a))
    
    plt.legend() 
    plt.show() 
            
    