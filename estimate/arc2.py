#2번 문제
import numpy as np
import random

def g(x):
    
    y=(1/np.sqrt(2*np.pi))*np.exp(-(x**2)*(1/2))
    return y

def E(n):
    N=0
    for _ in range  (n):
        i = random.random()
        N+=g(i)
    
    print(f"n={n} ---> {N/n}")
    return N/n

E(1000)
E(10000)
E(100000)
E(1000000)