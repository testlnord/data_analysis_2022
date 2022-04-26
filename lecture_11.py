import pandas as pd
import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt

# %%
# body fat percentage
# example from https://www.jmp.com/en_ch/statistics-knowledge-portal/t-test/two-sample-t-test.html
man = [13.3, 6.0, 20.0, 8.0, 14.0, 19.0, 18.0, 25.0, 16.0, 24.0, 15.0, 1.0, 15.0]
woman = [22.0, 16.0, 21.7, 21.0, 30.0, 26.0, 12.0, 23.2, 28.0, 23.0]

plt.hist(man, alpha=0.5, label='man')
plt.hist(woman, alpha=0.5, label='woman')
plt.legend(loc='upper right')
plt.title('Percentage of body fat')
plt.show()

# %%
all_pers = pd.concat((
    pd.DataFrame({"body_fat": man, 'sex': 'men'}),
    pd.DataFrame({"body_fat": woman, 'sex': 'women'}),
))
all_pers.reset_index(inplace=True, drop=True)
print(all_pers)
# %%
real_diff = np.mean(man) - np.mean(woman)
# %%
iterations_cnt = 10000
sample_diffs = []
for _ in range(iterations_cnt):
    fats_sample = all_pers['body_fat'].sample(frac=1, replace=False).reset_index(drop=True)
    sample_man_mean = fats_sample[all_pers['sex'] == 'men'].mean()
    sample_woman_mean = fats_sample[all_pers['sex'] == 'women'].mean()
    sample_diffs.append(sample_man_mean - sample_woman_mean)

# %%
pd.Series(sample_diffs).plot.hist()
# %%
p_left = len([x for x in sample_diffs if x < real_diff]) / len(sample_diffs)
print(p_left)
# %%
p_value = min(p_left, 1 - p_left) * 2
print(p_value)
# %%
# permutation test!!!

# %%
sigma1 = np.var(man)
sigma2 = np.var(woman)
sigma = ((len(man) - 1) * sigma1 + (len(woman) - 1) * sigma2) / (len(man) + len(woman) - 2)
t_stat = real_diff / sigma ** (0.5) / (1 / len(man) + 1 / len(woman)) ** (0.5)

# %%
df = len(man) + len(woman) - 2
zero_hypoth_t_dist = t(df=df)

# %%
p_val_t = 2 * min(zero_hypoth_t_dist.cdf(t_stat), 1 - zero_hypoth_t_dist.cdf(t_stat))
print(p_val_t)
# %%
