from scipy.stats import t, norm, binom, beta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
1. формулируем гипотезы
Нулевая гипотеза - разницы нет
Альтернативная гипотеза - разница есть 
2. В предположении о том что наша нулевая гипотеза верна 
   на сколько вероятно встретить те данные, что у нас есть, или более экстремальные?
   То есть те, которые еще сильнее отклоняются от нулевой гипотезы.
3. Вычесленная вероятность называет p-value 
4. Сравниваем наш p-value с некоторыми порогом. alpha - уровень
5. Отвергаем или не отвергаем нулевую гипотезу
"""

# %%
fair_coin_prob = 0.5
simple_sample = binom.rvs(size=100, p=0.3, n=1)


# %%
def plot_function(func, x_min=0, x_max=10, steps=1000):
    x = np.linspace(x_min, x_max, steps)
    y = func(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    # plt.show()
    return ax


# %%
a = (len(simple_sample) * fair_coin_prob)
b = len(simple_sample) - a
hypothesis_0_world = beta(a=a, b=b)
ax = plot_function(lambda x: hypothesis_0_world.pdf(x), 0, 1)
ax.axvline(simple_sample.mean())
plt.show()
# %%
plot_function(lambda x: hypothesis_0_world.cdf(x), 0, 1)
plt.show()
# %%
"""
Все про то что я вам рассказал про p-value правда, но я немного напутал с тем как оно считается.
Различие (альтернатинвая гипотеза) может быть как одно сторонним так и двусторонним.
Двусторонняя альтернативная гипотеза - есть какое-то отличие, не важно в большую или меньшую сторону.
В нашем примере с монеткой мы проверяем ялвяется ли она "честной" или нет, нам не важно на сколько она нечестная.
Односторонняя альтернативная гипотеза формулируется так, чтобы заранее зафиксировать отличие, которое мы ожидаем:
в большую или меньшую сторону. 
То есть в нашем случае это "монетка нечестная и орел на ней выпадает реже чем надо" или "монетка нечестная и орел 
на ней выпадает чаще чем надо."
В зависимости от сформулированной альтернативной гипотезы у нас немного поразному будет вычисляться p-value.
Ведь p-value это вероятность встретить те данные, что у нас есть, или более экстремальные.
Из-за разной постановки вопроса у нас по-разному будет формулироваться "экстремальность".
"""
def p_value_less(hyp0dist, sample_value):
    # экстремальными значениями будут те что меньше
    # cdf нам возвращает как раз вероятность увидеть значение sample_value или меньше
    return hyp0dist.cdf(sample_value)

def p_value_more(hyp0dist, sample_value):
    # экстремальными значением будут те что больше
    # cdf нам возвращает вероятность увидеть значение sample_value или __меньше__.
    # поэтому нам нужно вычесть её значение из 1, чтобы получить вероятность обратного события
    return 1 - hyp0dist.cdf(sample_value)

def p_value_two_sided(hyp0dist, sample_value):
    # экстремальными значениями будут то, что лежат далеко от центра
    # поэтому мы проверяем насколько удивительным является отклонение как в большую
    # так и в меньшую сторону. И берем самое удивительное из них. Вероятность которого наименьшая
    # поэтому min.
    # А на 2 мы умножаем, потому, что проверяем оба конца.
    return 2*min(hyp0dist.cdf(sample_value),
                 1 - hyp0dist.cdf(sample_value))

# %%
sample_p = simple_sample.mean()
p_val = p_value_two_sided(hypothesis_0_world, sample_p)
print(p_val)
# %%
simple_sample_small = np.array([0,0,0,0,0,0,0,1,1,1])
a = (len(simple_sample_small) * fair_coin_prob)
b = len(simple_sample_small) - a
hypothesis_0_world = beta(a=a, b=b)
ax = plot_function(lambda x: hypothesis_0_world.pdf(x), 0, 1)
ax.axvline(x=simple_sample_small.mean())
plt.show()
small_sample_p = simple_sample_small.mean()
p_val = p_value_two_sided(hypothesis_0_world, small_sample_p)
print(p_val)
#%%
