import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math

nvec = (1, 2, 5, 10, 100, 1000) # numbers of RVs to be averaged and standardized
K = 10000 # number of samples
# parameters for U[a,b]
a = 0.0
b = 10.0
mu = 5 #mean of U[a,b]
sigma = math.sqrt(25/3) #standard deviation of U[a,b]
random_x = np.random.uniform(a,b,K)
# empirical CDF
def ecdf(x):
	xs = np.sort(x)
	ys = np.arange(1, len(xs)+1)/float(len(xs))
	return xs, ys
xs,ys = ecdf(random_x)
xf = np.linspace(-5,5,100)
F = stats.norm.cdf(xf) #values of standard noraml CDF

for n in nvec:
	sample = np.random.uniform(a,b,(K,n))
	Sn = np.sum(sample,axis=1)
	Zn = (Sn - n * mu) / (sigma * np.sqrt(n))
    # sum of K samples of uniform RV~U[a,b]
    # calculate Z
    # calculate empirical CDF (eCDF) of Z
	xs,ys = ecdf(Zn)
	plt.plot(xs,ys,label=f'n={n}')
    # plot eCDF and F
plt.plot(xf, F, label='Standard Normal CDF', linestyle='--', color='black')
plt.xlabel('x')
plt.ylabel('CDF')
plt.title('Empirical CDF vs Standard Normal CDF')
plt.legend()
plt.show()
