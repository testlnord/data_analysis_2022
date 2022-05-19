import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, norm, ttest_1samp, binom


#%%
k = binom.rvs(n=1, p=0.3, size = 150)
for prop in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]:
    print(prop, ttest_1samp(k, prop))

#%%
n1 = norm.rvs(size=100, loc=1)
n2 = norm.rvs(size=100, loc=1.1)
ttest_ind(n1, n2)

#%%
# p-hacking
# bottomlining
# READ https://en.wikipedia.org/wiki/Data_dredging
p_vals = []
for _ in range(1000):
    n1 = norm.rvs(size=100)
    n2 = norm.rvs(size=100)
    p_vals.append(ttest_ind(n1, n2).pvalue)
#%%
pd.Series(p_vals).plot.hist()

#%%
import matplotlib.pyplot as plt
#%%
means = []
for _ in range(1000):
    means.append(norm.rvs(size=10).mean())
plt.plot(range(1000), means)
#%%
means = []
for _ in range(1000):
    means.append(norm.rvs(size=100).mean())
plt.plot(range(1000), means)