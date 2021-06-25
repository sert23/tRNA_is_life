# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import math
import numpy as np



file_path = "/Users/ernesto/PycharmProjects/tRNA_is_life/graph_scripts/radar_plot/HL5_anticodon.txt"

exp_df = pd.read_csv(file_path, sep="\t")

# Set data
df = pd.DataFrame({
    'group': ['A', 'B', 'C', 'D'],
    'var1': [38, 1.5, 30, 4],
    'var2': [29, 10, 9, 34],
    'var3': [8, 39, 23, 24],
    'var4': [7, 31, 33, 14],
    'var5': [28, 15, 32, 14]
})

print(df.tail())
print(exp_df.T.head())
t_df = exp_df.T
t_df.columns = t_df.iloc[0]
t_df = t_df[1:]
t_df = t_df.reindex(sorted(t_df.columns), axis=1)
t_df = t_df+1
t_df = t_df.applymap(math.log10)

# exit()


# number of variable
categories = list(t_df)
N = len(categories)

# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values_dict = {}
for i,row in t_df.iterrows():
    # print(t_df.loc[i].columns)
    # print(t_df.loc[i].values.flatten().tolist())
    # exit()
    values = t_df.loc[i].values.flatten().tolist()
    values += values[:1]
    # print(row[0])
    # print(row.name)
    values_dict[row.name] = values

# exit()
maxi = t_df.max().max()


# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
ax = plt.subplot(111, polar=True)

# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories, color='grey', size=8)

# Draw ylabels
ax.set_rlabel_position(0)
# increment = maxi/float(4)3
real_maxi = 10**maxi
possible_steps = [10,100,1000,10000,100000,1000000,10000000]
steps = []
for s in possible_steps:
    if s < real_maxi:
        steps.append(s)
        last_small = True
    if s > real_maxi and last_small:
        steps.append(s)
        last_small = False

trans_steps = [math.log10(x) for x in steps]
possible_ticks = ["10","100","1K","10K","100K","1M","10M"]

ticks = possible_ticks[:len(steps)]



# plt.yticks([10, 20, 30], ["10", "20", "30"], color="grey", size=7)
plt.yticks(trans_steps, ticks, color="grey", size=7)
plt.ylim(0, max(trans_steps)+0.10*max(trans_steps))


# Plot data
for sample,values in values_dict.items():
    print(sample)
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=sample)

# ax.legend()
# plt.legend(loc=1)
plt.legend(loc='lower right', bbox_to_anchor=(0.9, -0.1, 0.6, 0.8))

# Fill area
# ax.fill(angles, values, 'b', alpha=0.1)

# Show the graph
plt.show()