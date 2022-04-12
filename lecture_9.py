import pandas as pd
import numpy as np
from scipy.stats import binom, norm

# %%
sample = binom.rvs(p=0.4, n=1, size=1000)
# %%

# %%
means = [binom.rvs(p=0.4, n=1, size=100).mean() for _ in range(1000)]
pd.Series(means).plot.hist()
# %%
p_sample = sample.mean()
se_sample = (p_sample * (1 - p_sample) / len(sample)) ** (0.5)
norm.interval(loc=p_sample, scale=se_sample, alpha=0.95)
# %%
# как зависит ширина интервала от пропорции
proportions = np.linspace(0.01, 0.99, 30)
lows = []
highs = []
for prop in proportions:
    sample = binom.rvs(p=prop, n=1, size=1000)
    p_sample = sample.mean()
    se_sample = (p_sample * (1 - p_sample) / len(sample)) ** (0.5)
    low, high = norm.interval(loc=p_sample, scale=se_sample, alpha=0.95)
    lows.append(low)
    highs.append(high)
# %%
props_cis = pd.DataFrame({'prop': proportions,
                          'low': lows,
                          'high': highs})
props_cis['width'] = props_cis['high'] - props_cis['low']
props_cis.plot(x='prop', y='width')

# %%
# small proportion, z-interval
sample_rare_small = pd.Series([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
p_sample = sample_rare_small.mean()
se_sample = (p_sample * (1 - p_sample) / len(sample_rare_small)) ** (0.5)
low, high = norm.interval(loc=p_sample, scale=se_sample, alpha=0.95)
# граница интервала может выходить за разумный предел
print(low)
#%%
# интервалы на основе beta-распределения
sample = binom.rvs(p=0.4, n=1, size=1000)
x = sum(sample)
n = len(sample)
from scipy.stats import beta
beta.interval(alpha=0.95, a = x + 1/2, b=n-x + 1/2)
#%%
# интервалы на основе beta-распределения для редких событий
beta.interval(alpha=0.95, a = sum(sample_rare_small) + 1/2,
              b=len(sample_rare_small)-sum(sample_rare_small) + 1/2)
#%%
# пример нарисованного горизонтального барчарта с доверительным интервалом
import matplotlib.pyplot as plt
sample = binom.rvs(p=0.4, n=1, size=20)
x = sum(sample)
n = len(sample)
fig, ax = plt.subplots()
ax.barh(0.0, x/n)
ax.set_ylim(-2, 2)
low, high = beta.interval(alpha=0.95, a = x + 1/2, b=n-x + 1/2)
# много времени я потратил в этом месте, чтобы выяснить, что для не семметричных интервалов нужно передать массив из
# двух массивов: отступы влево и отсутпы вправо. Длина каждого должна соответстовать количеству точек
ax.errorbar(x/n, 0, xerr=[[x/n - low], [high-x/n]], fmt='or')
ax.set_title('bar with error')
plt.show()
#%%
