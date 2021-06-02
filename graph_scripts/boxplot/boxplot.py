# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import math
import numpy as np
import os
import sys

args = sys.argv

file_path = sys.argv[1]
#
#file_path = "/Users/ernesto/PycharmProjects/tRNA_is_life/graph_scripts/boxplot/boxplot-violin_FL.txt"

file_folder = "/".join(file_path.split("/")[:-1])

image_path = os.path.join(file_folder, "box_plot.png")
image_path_log = os.path.join(file_folder, "box_plot_log.png")

exp_df = pd.read_csv(file_path, sep="\t")

print(exp_df.head())
# print(exp_df.columns)
column1 = exp_df.columns[1]
column2 = exp_df.columns[2]
columns = list(exp_df.columns)[1:]

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid")
df = sns.load_dataset('iris')
melted_df = pd.melt(exp_df, value_vars=columns)
print(melted_df.tail())
print(melted_df["variable"].value_counts())
# melted_df = pd.melt(exp_df, id_vars=['A'], value_vars=['B'])
# print(df.tail())

# log_df = melted_df.applymap(math.log10)



# Usual boxplot
ax = sns.boxplot(x='variable', y='value', data=melted_df)
# ax.set(yscale="log")
# Add jitter with the swarmplot function
ax = sns.swarmplot(x='variable', y='value', data=melted_df, color="grey")
figure = plt.gcf()

plt.xlabel('')
plt.ylabel('')

figure.set_size_inches(8, 6)
plt.savefig(image_path, dpi=300)

# log axis

ax = sns.boxplot(x='variable', y='value', data=melted_df)
ax.set(yscale="log")
# Add jitter with the swarmplot function
ax = sns.swarmplot(x='variable', y='value', data=melted_df, color="grey")
figure = plt.gcf()

plt.xlabel('')
plt.ylabel('')
figure.set_size_inches(8, 6)
plt.savefig(image_path_log, dpi=300)
