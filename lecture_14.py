import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gamma, sem, t
#%%
"""
 1 | 2 | 3 | 4 | 5 | 6
----------------------
1/6|1/6|1/6|1/6|1/6|1/6

  O | P 
 -------
 0.7|0.3

"""

values = pd.Series([0, 1])
probs = pd.Series([0.7, 0.3])
#%%
sample = values.sample(n=100, weights=probs, replace=True)
print(sample.mean())
#%%
g_sample = gamma.rvs(1, 3, size=100)
#%%
pd.Series(g_sample).plot.hist()
#%%
g_sample_mean = g_sample.sum() / len(g_sample)
#%%
bs_means = []
for i in range(1000):
    bs_mean = pd.Series(g_sample).sample(n=len(g_sample), replace=True).mean()
    bs_means.append(bs_mean)
#%%
fig, ax = plt.subplots()
pd.Series(bs_means).plot.hist(ax=ax)
ax.axvline(x=g_sample_mean, c='red')
plt.show()
#%%
# 95% CI : low 2.5% , high 97.5%
low_ci = pd.Series(bs_means).quantile(q=0.025)
high_ci = pd.Series(bs_means).quantile(q=0.975)
print(low_ci, high_ci)
#%%
bs_means.sort()
#%%
low_ci = bs_means[round(0.025 * len(bs_means))]
high_ci = bs_means[round(0.975 * len(bs_means))]
print(low_ci, high_ci)

#%%
# hitriy sample
# A: 1, 2, 10
# B: 1, 1, 0
# C: 3, 43
# D: 2, 2, 2
d = pd.DataFrame({'people':list("AAABBBCCDDD"),
                  'carrots':[1,2,10, 1,1,0, 3, 43, 2,2,2]})
print(d.head())
#%%
car_mean = d.carrots.mean()
#%%
people = pd.Series(d.people.unique())
bs_car_means = []
for i in range(100):
    s = people.sample(n=len(people), replace=True)
    total_l = 0
    total_s = 0
    for p in s:
        c = d['carrots'][d['people'] == p]
        c_l = len(c)
        c_s = sum(c)
        total_s += c_s
        total_l += c_l
    bs_car_means.append(total_s/total_l)
#%%

fig, ax = plt.subplots()
pd.Series(bs_car_means).plot.hist(ax=ax)
ax.axvline(x=car_mean, c='red')
plt.show()
#%%
low_ci = pd.Series(bs_car_means).quantile(q=0.025)
high_ci = pd.Series(bs_car_means).quantile(q=0.975)
print(low_ci, high_ci)
#%%
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), sem(a)
    h = se * t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h
mean_confidence_interval(d['carrots'])