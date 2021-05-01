import sys
import matplotlib.pyplot as plt
import matplotlib
import os
import pandas as pd
from matplotlib import cm
import numpy as np
import seaborn as sns
import numpy as np


np.random.seed(0)
# sns.set_theme()
uniform_data = np.random.rand(10, 12)

# args = sys.argv

file_path = sys.argv[1]

# file_path = "/Users/ernesto/PycharmProjects/tRNA_is_life/graph_scripts/FC_heatmap/heatmap_HB-GBM.txt"
title = "hehe"
file_base = ".".join(file_path.split(".")[:-1])
file_name = file_base.split("/")[-1]

#load with pandas

exp_df = pd.read_csv(file_path, sep="\t")
# print(exp_df.columns)
names = exp_df.columns.values[1:]
groups = exp_df.iloc[0].values[1:]
group_dict = {}
collapsed_groups = []

for i,name in enumerate(names):
    # print(name,groups[i])
    group_dict[name] = groups[i]
    if groups[i] not in collapsed_groups:
        collapsed_groups.append(groups[i])

reference_group = collapsed_groups[0]
reference_samples = [s for s in names if group_dict[s]==reference_group]

exp_df = exp_df.set_index('name')
exp_df = exp_df.drop("group")
exp_df = exp_df.astype(float)
sums = exp_df.sum(0)
exp_df = exp_df.div(sums, axis='columns')*1000000

# print(ref_df.head())
# calculate average value for reference group
ref_df = exp_df[reference_samples]
ref_av = ref_df.mean(axis=1)
# print(ref_df.head())
# print(ref_av)
# print(exp_df.head())
# exp_df = exp_df + 1
# ref_av = ref_av +1
exp_df = exp_df + 1
ref_av = ref_av + 1
FC_df = exp_df.divide(ref_av,0)
logFC_df = FC_df.apply(np.log2)
logFC_df = logFC_df.replace([np.inf, -np.inf], np.nan)

# print(FC_df.head())
# print(collapsed_groups)
to_plot = FC_df.T
to_plot = FC_df.T.head()
to_plot = FC_df.iloc[:10,:10].T
to_plot = logFC_df.iloc[:20,:20].T
to_plot = logFC_df.iloc[:100,:20].T
to_plot = logFC_df.T
print(list(logFC_df.max()))

colors = ["#FF0B04", "#4374B3"]
# Set your custom color palette
# sns.set_palette(sns.color_palette(colors))
# sns.set_palette(sns.color_palette(colors))
palette = sns.color_palette()
color_dict = {}
labels = []

for index in to_plot.index:
    # print(index)
    g = group_dict[index]
    labels.append(g)
    n = collapsed_groups.index(g)
    color = palette[n]
    # print(color)
    color_dict[index] = color

color_rows = pd.Series(color_dict)
label_pal = sns.color_palette()
label_lut = dict(zip(map(str, collapsed_groups), label_pal))
# label_colors = pd.Series(labels, index=df.columns).map(network_lut)


x,y = to_plot.shape
default_x = x/float(4)
default_y = y/float(4)


# regular plot

fig, ax = plt.subplots(figsize=(default_y, default_x))
sns.heatmap(to_plot, cmap="gist_rainbow",)

plt.savefig(file_base + "_all.png")



# 20 highest abs FC


logFC_df["FC"] = logFC_df.mean(axis=1, numeric_only=True, skipna=True).abs()
to_plotFC = logFC_df.nlargest(20, columns=['FC'])
to_plot = to_plotFC.T
to_plot = to_plot.drop("FC",axis=0)
x,y = to_plot.shape
default_x = x/float(4)
default_y = y/float(4)

fig, ax = plt.subplots(figsize=(default_y, default_x))
sns.heatmap(to_plot, cmap="gist_rainbow",)
plt.savefig(file_base + "_FC.png")
exit()
