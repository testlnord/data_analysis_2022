import matplotlib.pyplot as plt
import pandas as pd

fig, ax = plt.subplots()

test_df = pd.DataFrame({'x': [1, 1.5],
                        'y': [1, 1],
                        'size': [2000, 4000]})

ax.scatter(test_df['x'], test_df['y'], s=test_df['size'])
ax.set_xlim(0.5, 2)
#%%
