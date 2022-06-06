import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, shapiro, t


"""
common requirement - independence and identical distribution of values in the sample
"""

#%%
"""
Normality. 
Shapiro-Wilk test 
 To check normality of data we can use Shapiro–Wilk Test. The null hypothesis for this test is — the distribution of the data sample is normal.
 https://en.wikipedia.org/wiki/Shapiro%E2%80%93Wilk_test
 Like most statistical significance tests, if the sample size is sufficiently large this test may detect even trivial 
 departures from the null hypothesis (i.e., although there may be some statistically significant effect, 
 it may be too small to be of any practical significance); 
"""
data = norm.rvs(loc=2.5, scale=2, size=100)
shapiro_test = shapiro(data)
print(shapiro_test)

data_t = t.rvs(loc=12, scale=2, df = 12, size=100)
shapiro_test_t = shapiro(data_t)
print(shapiro_test_t)

#%%
"""
Test for proportion 
Z-test
https://en.wikipedia.org/wiki/Z-test
- data should be normal. Generally, one appeals to the central limit theorem to justify assuming that a test statistic varies normally. There is a great deal of statistical research on the question of when a test statistic varies approximately normally. If the variation of the test statistic is strongly non-normal, a Z-test should not be used.
- Nuisance parameters should be known or estimated with high precision. Like variance

"""
from statsmodels.stats.proportion import proportions_ztest
data = [1, 1, 1, 1, 0, 0, 0, 0, 0]
stat, pval = proportions_ztest(sum(data), len(data), 0.5)
print(pval)

#%%
"""
T-test
https://en.wikipedia.org/wiki/Student%27s_t-test
- Normal data
"""
#%%

"""
ANOVA, also known as analysis of variance, is used to compare multiple (three or more) samples with a single test
Null: All pairs of samples are same i.e. all sample means are equal
Alternate: At least one pair of samples is significantly different
https://www.pythonfordatascience.org/anova-python/

"""
df = pd.read_csv("https://raw.githubusercontent.com/researchpy/Data-sets/master/difficile.csv")
df.drop('person', axis= 1, inplace= True)

# Recoding value from numeric to string
df['dose'].replace({1: 'placebo', 2: 'low', 3: 'high'}, inplace= True)

df.info()

import scipy.stats as stats

stats.f_oneway(df['libido'][df['dose'] == 'high'],
               df['libido'][df['dose'] == 'low'],
               df['libido'][df['dose'] == 'placebo'])

#%%
tbl = [[1, 9],[11, 3]]
stats.fisher_exact(tbl)
#%%
stats.chi2_contingency(tbl)
#%%
