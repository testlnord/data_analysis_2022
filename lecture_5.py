import pandas as pd
from scipy.stats import norm
from matplotlib import pyplot as plt
import numpy as np
#%%

def plot_function(func, x_min=0, x_max=10, steps=1000):
    x = np.linspace(x_min,x_max, steps)
    y = func(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()

plot_function(lambda x: norm.pdf(x, 5, 1))
plot_function(lambda x: norm.pdf(x, 5, 3))



#%%
norm.stats(5, 1)
x_norm = norm.rvs(5, 1, size=100)
x_norm.var()

#%%
# распределение стьюдента
#%%
from scipy.stats import t
sample = t.rvs(df=1, loc=0, scale=3, size = 1000)
fig, ax = plt.subplots()
ax.plot(range(1000), sample)

#%%
m = sample.mean()
v = sample.var()
print(m, v)
plot_function(lambda x: norm.pdf(x, m, v), -10000, 10000)
#%%
plot_function(lambda x: t.pdf(x, loc=0, scale=3, df=1), -100, 100)

#%%
plot_function(lambda x: norm.pdf(x, loc=0, scale=3), -100, 100)

#%%

sample = norm.rvs(loc=0, scale=3, size = 1000)
fig, ax = plt.subplots()
ax.plot(range(1000), sample)

#%%
from scipy.stats import beta
plot_function(lambda x: beta.pdf(x, a=3, b=5), 0, 1)


#%%
from scipy.stats import binom
means = []

for i in range(1000):
    m = binom.rvs(n=1, p=0.98, size=100).mean()
    means.append(m)

fig, ax = plt.subplots()
ax.hist(means)
plt.show()
#%%
plot_function(lambda x: beta.pdf(x, a=980, b=20), 0, 1)
#%%
plot_function(lambda x: beta.pdf(x, a=1, b=1), 0, 1)