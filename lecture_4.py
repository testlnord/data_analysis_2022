#%%
import pandas as pd
from scipy.stats import binom, norm, geom
import numpy as np
# some stuff for plotting
import matplotlib.pyplot as plt
"""
https://docs.scipy.org/doc/scipy/reference/stats.html
Main stats.* methods
- rvs: Random Variates !!!
- pdf: Probability Density Function !!!
- cdf: Cumulative Distribution Function
- sf: Survival Function (1-CDF)
- ppf: Percent Point Function (Inverse of CDF)
- isf: Inverse Survival Function (Inverse of SF)
- stats: Return mean, variance, (Fisher’s) skew, or (Fisher’s) kurtosis 
- moment: non-central moments of the distribution
"""
#%%

fig, ax = plt.subplots(1, 1)
x = binom.rvs(n=1, p=0.2, size=100)
ax.hist(x)
#%%
print(x.mean())
print(binom.stats(n=1, p=0.2))
#%%
means = []
sizes = []
for size in range(10, 500, 20):
    m = binom.rvs(n=1, p=0.2, size=size).mean()
    sizes.append(size)
    means.append(m)
#%%
fig, ax = plt.subplots()
ax.plot(sizes, means)

#%%
fig, ax = plt.subplots()
x = norm.rvs(160, 15, size = 1000)
ax.hist(x)

#%%


def plot_function(func, x_min=0, x_max=10, steps=1000):
    x = np.linspace(x_min,x_max, steps)
    y = func(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()

plot_function(lambda x: norm.pdf(x, 160, 15), 110, 210)


#%%
from scipy.stats import gamma
plot_function(lambda x: gamma.pdf(x, 2))

#%%
gamma.stats(2)
#%%
plot_function(lambda x: gamma.pdf(x, 1))
"""
Тут я показывал вам gamma(1) и говорил, что это распределение силы извержений. 
Но это не совсем так.

Распределение, которое показывает, что большое встречается редко, а маленькое часто это распределение Парето.
Вы наверное слышали про закон Парето 80/20. Вот это оттуда.
Примеров много приводить не буду, лучше просто пошлю вас в википедию:
https://en.wikipedia.org/wiki/Pareto_distribution#General
Гамма распределение – это распределение каких-то интервалов между событиями. Или количества дождя (ведь время как вода) 
https://en.wikipedia.org/wiki/Gamma_distribution#Occurrence_and_applications

"""
#%%
from scipy.stats import pareto
plot_function(lambda x: pareto.pdf(x, 1.61))
#%%
"""
Тут я напутал из-за названий. 
zipf - это, оказывается, зета-распределение. Оно получается, когда у нас бесконечно много "слов".
zipfian - это само распределение Ципфа, оно появилось в scipy.stats относительно недавно.
Вообще распределение Ципфа выводится из распределения Парето. Они и правда очень похожи и по виду и по смыслу. 
"""
from scipy.stats import zipfian

x = zipfian.rvs(1, 10 , size=100)
fig, ax = plt.subplots()
ax.hist(x)

#%%
