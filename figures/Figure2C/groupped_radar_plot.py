# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import math
import numpy as np
import matplotlib
import sys
import os

# parameters

linewidth = 1

# colors and labels

# paired colors ['#a6cee3', '#1f78b4',
#  '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c',
#  '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a', '#ffff99', '#b15928']

label_dict = { "HL5_SSIII_untreated":"SuperScript III untreated",
             "HL5_SSIII_DMtreated": "SuperScript III DM-treated",
             "HL5_mRT_untreated" : "MarathonRT untreated",
               "HL5_mRT_DMtreated" : "MarathonRT DM-treated"

}

# color_dict = { "HL5_SSIII_untreated":"#cab2d6",
#              "HL5_SSIII_DMtreated": "#A00078",
#              "HL5_mRT_untreated" : "#b2df8a",
#                "HL5_mRT_DMtreated" : "#00A03C"
#
# }

color_dict = { "HL5_SSIII_untreated":"#fb9a99",
             "HL5_SSIII_DMtreated": "#A00078",
             "HL5_mRT_untreated" : "#b2df8a",
               "HL5_mRT_DMtreated" : "#00A03C"

}

#input_file

file_path = sys.argv[1]
# file_path = "HL5_anticodon.txt"
# image_path = "radar_plot.png"
# base_path = os.path.join(file_path.split("/")[:-1])
base_path = ".".join(file_path.split(".")[:-1])

# image_path_log = os.path.join(base_path, "radar_plot_log.png")
image_path_log = base_path + "_radar_plot.png"

exp_df = pd.read_csv(file_path, sep="\t")







# grouping by aminoacid




print(exp_df.T.head())


t_df = exp_df.T
t_df.columns = t_df.iloc[0]
t_df = t_df[1:]
t_df = t_df.reindex(sorted(t_df.columns), axis=1)

print(t_df.columns)

cols = t_df.columns

aminoacids = []
new_df = pd.DataFrame()

for c in cols:
    aa = c[:-3]
    if aa not in aminoacids:
        aminoacids.append(aa)
        matching_cols = [c for c in cols if c.startswith(aa)]
        print(aa)
        # print(matching_cols)
        aa_df = t_df[t_df.columns.intersection(matching_cols)]
        if new_df.empty:
            # print("new")
            new_df[aa] = aa_df.sum(axis=1)
        else:
            # print("not new")
            new_df[aa] = aa_df.sum(axis=1).values
            # new_df = new_df.assign(e=pd.Series(np.random.randn(sLength)).values)

        # print(s)




t_df = new_df
t_df = t_df+1
pre_log_df = t_df
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
# possible_steps = [10,100,1000,10000,100000, 500000]
possible_steps = [10,100,1000,10000,100000,1000000,10000000]
steps = []
for s in possible_steps:
    if s < real_maxi:
        steps.append(s)
        last_small = True
    if s > real_maxi and last_small:
        steps.append(s)
        last_small = False

# hardcoding steps
steps = possible_steps[:5]

trans_steps = [math.log10(x) for x in steps]
possible_ticks = ["10","100","1K","10K","100K","1M","5M"]

ticks = possible_ticks[:len(steps)]



# plt.yticks([10, 20, 30], ["10", "20", "30"], color="grey", size=7)
plt.yticks(trans_steps, ticks, color="grey", size=7)
plt.ylim(0, max(trans_steps)+0.10*max(trans_steps))


# Plot data
for sample,values in values_dict.items():
    print(sample)
    ax.plot(angles, values, linewidth=linewidth, linestyle='solid', label=label_dict.get(sample), color=color_dict.get(sample))

# ax.legend()
# plt.legend(loc=1)
font = {
    # 'family' : 'normal',
        'weight' : 'bold',
        'size'   : 12}

matplotlib.rc('font', **font)
plt.xticks(fontsize=12, weight="bold" )
plt.legend(loc='lower right', bbox_to_anchor=(0.9, -0.1, 0.6, 0.8))

# Fill area
# ax.fill(angles, values, 'b', alpha=0.1)

# Show the graph
figure = plt.gcf()
figure.set_size_inches(10, 6)
plt.savefig(image_path_log, dpi=300)






exit()
