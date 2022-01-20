

"""
1. данные dict, list, str, tuple
2. числа float, int
3. функции
4. классы, объекты, методы
5. библиотеки
"""

a = 1
b = 1.0
# %%
c = 1.00000000000000000000000000000000000000000000000000000009
print(c)
# %%
a = 120983710948023984209384029384029384029384029384029384029834092830498
print(a ** (0.5))
# %%
a = 1.0999259563626271e+34
print(a % 10)
# %%
# динамическая VS статическая типизация
# %%
l1 = list()
l2 = []
l = [1, 2, 3, 4]
print(l)
# %%
t = tuple()
t2 = (1, 2, 3)
print(t2)
# %%
print(type(()))
print(type((1)))
print(type((1,)))
# %%
d1 = dict()
d2 = {}
d = {1: 1, (1, 2, 3): 3}
print(d)
# %%
s = {1, 3, 4, 1, 2, 3, 2, 1}
print(s)
1 in s  # faster
1 in l

# %%
# list - unhashable
# d[[1,2,3]] = 3

# %%
s1 = "1341'2"
s2 = '1234"2'
print(s1, s2)


# %%
def foo(a=3):
    print(a)


foo(2)
foo()


# %%
def foo(a=[]):
    a.append(1)
    print(a)


foo()
foo()


# %%
def foo(a, b):
    print(a, b)


foo(1, b=34)
foo(b=3, a=43)

#%%
class Azaza:
    def __init__(self):
        self.a = 32

azaza = Azaza()
print(azaza.a)
azaza.a = 53
print(azaza.a)
#%%
import numpy as np
import pandas as pd
df1 = pd.DataFrame({'name':['t1','t2','t3'],
                    'f':[30, 20,32],
                    'm':[23,342,1],
                    'n':[1, 313,32]})
print(df1)
"""
ключевые элементы:
1. строки и столбцы
2. индексы

"""
#%%
df2 = pd.DataFrame({
                    'f':[30, 20,32],
                    'm':[23,342,1],
                    'n':[1, 313,32]},
                   index=['t1','t2','t3']
                   )
print(df2)

#%%
print(df1.ndim)  # dimensions
print(df1.size)  # number of elements
print(df2.size)
print(len(df2))  # number of rows

#%%
iris = pd.read_csv('data/iris.csv')
print(iris.head())
