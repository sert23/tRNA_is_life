import sys
import matplotlib.pyplot as plt
import matplotlib
import os
import pandas as pd
from matplotlib import cm
import numpy as np
import seaborn as sns
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


# PLOT ALL

width_1 = 30
height_1 = 20
font_1_x = 15
font_1_y = 15

# PLOT SELECTED

width_2 = 10
height_2 = 10
font_2_x = 15
font_2_y = 15
features_to_select = 20

np.random.seed(0)
# sns.set_theme()



rainBow = cm.get_cmap('gist_rainbow', 200)
no_purple_cmap = ListedColormap(rainBow(np.linspace(0, 0.75, 256)))


# parameters
# args = sys.argv
if len(sys.argv)>1:
    file_path = sys.argv[1]
else:
    file_path = "/Users/ernesto/PycharmProjects/tRNA_is_life2/graph_scripts/FC_heatmap/heatmap_HB-GBM.txt"

file_base = ".".join(file_path.split(".")[:-1])
# file_name = file_base.split("/")[-1]

if len(sys.argv) > 2:
    n_features = int(sys.argv[2])
else:
    # n_features = 20
    n_features = features_to_select
# else:
cmin = None
# if len(sys.argv) > 3:
#     cmax = float(sys.argv[3])
# else:
cmax = None

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
#
# print(exp_df.head())
# exit()
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

# figure = plt.gcf()
#
# plt.axis('off')
# plt.plot(x, y, color='black', linewidth=1)
# plt.gca().set_position([0, 0, 1, 1])
# plt.savefig("image.png", dpi=100)


# fig, ax = plt.subplots(figsize=(default_y, default_x))
# fig, ax = plt.subplots(figsize=(width_1, height_1))
fig, ax = plt.subplots(figsize=(width_1, height_1))
fig.set_size_inches(width_1, height_1)
from matplotlib import rcParams

# figure size in inches
rcParams['figure.figsize'] = width_1, height_1

# sns.heatmap(to_plot, cmap=no_purple_cmap,vmin=cmin, vmax=cmax)
sns.set(rc={'figure.figsize':(width_1,height_1)})
cg = sns.clustermap(to_plot, cmap=no_purple_cmap,vmin=cmin, vmax=cmax)
# cg = sns.clustermap(to_plot, cmap=no_purple_cmap,vmin=cmin, vmax=cmax, height=height_1, aspect=height_1/float(width_1))
# cg = sns.clustermap(to_plot, cmap=no_purple_cmap,vmin=cmin, vmax=cmax, dendrogram_ratio=(.1, .1),)
cg.ax_col_dendrogram.set_visible(False)
sns.set(rc={'figure.figsize':(width_1,height_1)})
fig.set_size_inches(width_1, height_1)
x_ticks_size = font_1_x
y_ticks_size = font_1_y

for tick_label in cg.ax_heatmap.axes.get_yticklabels():
    tick_text = tick_label.get_text()
    # species_name = species.loc[int(tick_text)]
    tick_label.set_size(x_ticks_size)

for tick_label in cg.ax_heatmap.axes.get_xticklabels():
    tick_text = tick_label.get_text()
    # species_name = species.loc[int(tick_text)]
    tick_label.set_size(y_ticks_size)

# cg.ax_heatmap.axes.get_yticklabels()
#
# cg.set_xticklabels(cg.get_xmajorticklabels(), fontsize = 18)

# plt.xticks(rotation=45, fontsize=14, ha='right', rotation_mode='anchor')
# plt.yticks(fontsize=18)

# sns.set(font_scale = 2)
from matplotlib import rcParams

# figure size in inches
rcParams['figure.figsize'] = width_1, height_1
plt.gcf().set_size_inches(width_1, height_1)

plt.savefig(file_base + "_all.png", dpi=300)
# plt.show()
print(file_base + "_all.png")
# plt.savefig("/Users/ernesto/PycharmProjects/tRNA_is_life2/graph_scripts/FC_heatmap/heatmap_HB-GBM.png")

print("done")
plt.gcf().clear()


# n highest abs FC


logFC_df["FC"] = logFC_df.mean(axis=1, numeric_only=True, skipna=True).abs()
# selecting n_features (number of features)
to_plotFC = logFC_df.nlargest(n_features, columns=['FC'])
to_plot = to_plotFC.T
to_plot = to_plot.drop("FC",axis=0)
x,y = to_plot.shape
default_x = x/float(4)
default_y = y
# fig, ax = plt.subplots(figsize=(default_y, default_x))
# fig, ax = plt.subplots(figsize=(4, 35))
# figure = plt.gcf()
fig, ax = plt.subplots(figsize=(width_2, height_2))
cg = sns.clustermap(to_plot, cmap=no_purple_cmap, vmin=cmin, vmax=cmax, figsize=(default_x, default_y))
cg.ax_col_dendrogram.set_visible(False)

print(to_plot.head())

x_ticks_size = font_2_x
y_ticks_size = font_2_y

for tick_label in cg.ax_heatmap.axes.get_yticklabels():
    tick_text = tick_label.get_text()
    # species_name = species.loc[int(tick_text)]
    tick_label.set_size(x_ticks_size)

for tick_label in cg.ax_heatmap.axes.get_xticklabels():
    tick_text = tick_label.get_text()
    # species_name = species.loc[int(tick_text)]
    tick_label.set_size(y_ticks_size)

# plt.xticks(rotation=45, fontsize=14, ha='right', rotation_mode='anchor')
# plt.yticks(fontsize=18)
# fig, ax = plt.subplots(figsize=(width_2, height_2))
plt.gcf().set_size_inches(width_2, height_2)
plt.savefig(file_base + "_top" + str(n_features) + "_FC.png", dpi=300)
print(file_base + "_top" + str(n_features) + "_FC.png")
print("done")
exit()
