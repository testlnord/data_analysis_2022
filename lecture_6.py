"""
Долги
1. многомерные распределения
2. корреляция и ковариация
3. Квартет Энскомба

"""
import pandas as pd
titanic_data = pd.read_csv('data/titanic.csv')
#%%
titanic_data.head()

#%%
# guenea pigs' teeth
# https://rstudio-pubs-static.s3.amazonaws.com/83486_ab3fec0ede234d7183533dbdc0bdc73e.html
#%%
from scipy.stats import multivariate_normal
import numpy as np
import matplotlib.pyplot as plt
x2d = multivariate_normal([0.5, -0.2], [[2.0, 0.9],
                                        [0.9, 0.5]])
x, y = np.mgrid[-1:1:.01, -1:1:.01]
pos = np.dstack((x, y))
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.contourf(x, y, x2d.pdf(pos))

#%%
x2d_sample = x2d.rvs(size=100)
#%%
np.cov(np.transpose(x2d_sample)*2)
#%%
np.corrcoef(np.transpose(x2d_sample)*2)
#%%
pd.DataFrame({'a':x2d_sample[:,1],
              'b':x2d_sample[:,0]}).plot.scatter(x='a', y='b')

#%%
pd.DataFrame({'a':x2d_sample[:,1],
              'a2':x2d_sample[:,1]*-2}).plot.scatter(x='a', y='a2')
pd.DataFrame({'a':x2d_sample[:,1],
              'a2':x2d_sample[:,1]*-2}).corr()
#%%
# квартет Энскомба
# https://ru.wikipedia.org/wiki/%D0%9A%D0%B2%D0%B0%D1%80%D1%82%D0%B5%D1%82_%D0%AD%D0%BD%D1%81%D0%BA%D0%BE%D0%BC%D0%B1%D0%B0

#%%
import matplotlib.pyplot as plt
fig, (ax, ax2) = plt.subplots(2)
ax.plot([0, 1], [1, -2], c='red')
ax.fill_between([-2, 0], [-1.5, -1], [-1, .5], facecolor='green', alpha=0.5)
ax.scatter(x2d_sample[:, 0], x2d_sample[:, 1], c='#FFAA40')

ax.set_title('Test plot')
plt.show()
# plt.savefig('asdf.png')
#%%
fig, ax = plt.subplots()
ax.set_title('Titanic')
titanic_data_male_sur = titanic_data[(titanic_data['Sex'] == 'male')&(titanic_data['Survived']==1)]
titanic_data_female_sur = titanic_data[(titanic_data['Sex'] == 'female')&(titanic_data['Survived']==1)]
titanic_data_male_died = titanic_data[(titanic_data['Sex'] == 'male')&(titanic_data['Survived']==0)]
titanic_data_female_died = titanic_data[(titanic_data['Sex'] == 'female')&(titanic_data['Survived']==0)]
ax.scatter(titanic_data_male_sur['Age'], titanic_data_male_sur['Fare'],c='r', marker='o', label='Male')
ax.scatter(titanic_data_female_sur['Age'], titanic_data_female_sur['Fare'],c='g', marker='o', label='Female')
ax.scatter(titanic_data_male_died['Age'], titanic_data_male_died['Fare'],c='r', marker='x')
ax.scatter(titanic_data_female_died['Age'], titanic_data_female_died['Fare'],c='g', marker='x')

ax.legend()
ax.set_xlabel('Age')
ax.set_ylabel('Fare')
plt.show()

#%%
fig, ax = plt.subplots()
line_up, = ax.plot([1, 2, 3], label='Line 2')
line_down, = ax.plot([3, 2, 1], label='Line 1')
ax.legend([line_up, line_down], ['Line Up', 'Line Down'])