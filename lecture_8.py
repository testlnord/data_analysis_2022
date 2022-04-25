# Интервальные оценки. Доверительные интервалы.
from scipy.stats import t, norm, sem
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# %%
# define sample data
data = [12, 12, 13, 13, 15, 16, 17, 22, 23, 25, 26, 27, 28, 28, 29]

# create 95% confidence interval for population mean weight
dist_t = t(df=len(data) - 1, loc=np.mean(data), scale=sem(data))


# %%
def plot_function(func, x_min=0, x_max=10, steps=1000):
    x = np.linspace(x_min, x_max, steps)
    y = func(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    # plt.show()
    return ax


# %%
ax = plot_function(dist_t.pdf, 10, 30)
ax.vlines(dist_t.interval(alpha=0.99), ymin=0, ymax=0.2, colors='r')
plt.show()
# %%
# Доверительные интервалы. Иногда не накрывают реальное значение
original_norm = norm(3, 2)
fig, ax = plt.subplots()
for i in range(100):
    sample = original_norm.rvs(100)
    sample_interval = t.interval(alpha=0.9, df=99, loc=np.mean(sample), scale=sem(sample))
    ax.hlines(i, xmin=sample_interval[0], xmax=sample_interval[1])
ax.vlines(3, ymin=0, ymax=100)
ax.set_xlim(2, 4)
plt.show()

# %%

# Доверительные интервалы на выборке бОльшего размера
fig, ax = plt.subplots()
for i in range(100):
    sample = original_norm.rvs(1000)
    sample_interval = t.interval(alpha=0.9, df=999, loc=np.mean(sample), scale=sem(sample))
    ax.hlines(i, xmin=sample_interval[0], xmax=sample_interval[1])
ax.vlines(3, ymin=0, ymax=100)
ax.set_xlim(2, 4)
plt.show()
# %%
# %%
# Доверительные интервалы на выборке бОльшего размера и с бОльшим уровнем доверия
fig, ax = plt.subplots()
for i in range(100):
    sample = original_norm.rvs(1000)
    sample_interval = t.interval(alpha=0.99, df=999, loc=np.mean(sample), scale=sem(sample))
    ax.hlines(i, xmin=sample_interval[0], xmax=sample_interval[1])
ax.vlines(3, ymin=0, ymax=100)
ax.set_xlim(2, 4)
plt.show()

# %%
# %%
# Доверительные интервалы на выборке бОльшего размера для распределения с бОльшей дисперсией
original_norm_wide = norm(3, 4)

fig, ax = plt.subplots()
for i in range(100):
    sample = original_norm_wide.rvs(1000)
    sample_interval = t.interval(alpha=0.9, df=999, loc=np.mean(sample), scale=sem(sample))
    ax.hlines(i, xmin=sample_interval[0], xmax=sample_interval[1])
ax.vlines(3, ymin=0, ymax=100)
ax.set_xlim(2, 4)
plt.show()
