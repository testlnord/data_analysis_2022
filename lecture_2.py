# рассказать про разрешение имен при импорте
import numpy as np

import test_package

#%%
# pandas
import pandas as pd

iris = pd.read_csv('data/iris.csv')
iris.head()
#%%

# выбрать колонку
iris['variety']
#%%
# 2 колонки
iris[['variety', 'petal.length']].head()
#%%
# фильтр рядов
iris[iris['petal.length'] > 2]
#%%
# и колонки и ряды loc
# iris[iris['petal.length'] > 2]['variety'].unique()
iris.loc[iris['petal.length']>2, 'variety'].unique()
#%%
iris.loc[iris['petal.length']>2, ['variety', 'sepal.width']].head()
#%%
s1 = pd.Series([1,2,3,4,5])
s1 *2
s1 > 3
((s1 % 2) == 1 ) & (s1 > 3)
((s1 % 2) == 1 ) | (s1 > 3)
~((s1 % 2) == 1 )
# не забывайте расставлять скобки
#%%
iris.loc[(iris['petal.length']>2) & (iris['sepal.length']>2), ['variety', 'sepal.width']].head()
#%%
odds_flag = [i % 2 == 1 for i in range(len(iris))]
iris[odds_flag]

#%%
# доступ по индексу iloc
iris.iloc[3]
iris.iloc[3, 2]
iris.iloc[:, 2]
iris.iloc[[1,2,3,100], 2]
iris.iloc[[1,2,3,100], [4,2]]

#%%
# добавить колонку
df = pd.DataFrame({'a':[1,2,3,4,5],
                   'b':[0.3, 0.01,12,0.3,11.5],
                   'c':['a','b','c','d','e']})
df
#%%
df['e'] = df['a']**2
df
#%%
import numpy as np

df['b'] = df['e'].apply(np.log)
df
# изменить
#%%
df.loc[df['a'] > 2, 'b'] = 3
df.loc[df['a'] > 3, 'b'] = df.loc[df['a'] > 3, 'a'] ** 0.3
df

#%%
# должен быть установлен matplotlib
df.plot()
df.plot(kind='scatter', x='a', y = 'b')
#%%
def var2color(variety_name):
    if variety_name == 'Setosa':
        return '#FF0000'
    elif variety_name == 'Versicolor':
        return '#00FF00'
    elif variety_name == 'Virginica':
        return '#0000FF'
    return '#333333'

iris['color'] = iris['variety'].apply(var2color)
iris.plot(kind='scatter', x='petal.length', y='petal.width', c='color')

#https://colorbrewer2.org/


# HW: нарисовать scatter plot для данных о пассажирах выживших на титанике
# выберете пассажиров второго класса, старше 30 лет
# нарисуйте зависимость возраста и тарифа
# цветом кодируйте пол пассажира