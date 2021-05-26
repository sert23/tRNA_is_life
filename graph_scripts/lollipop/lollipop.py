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

# file_path = "/Users/ernesto/PycharmProjects/tRNA_is_life/graph_scripts/lollipop/lollipop_example.txt"

file_folder = "/".join(file_path.split("/")[:-1])

image_path = os.path.join(file_folder, "lollipop.png")

exp_df = pd.read_csv(file_path, sep="\t")

print(exp_df.head())
# print(exp_df.columns)
column1 = exp_df.columns[1]
column2 = exp_df.columns[2]

# exit()


my_range=range(1,len(exp_df.index)+1)
ordered_df = exp_df.sort_values(by=column1)

plt.hlines(y=my_range, xmin=ordered_df[column1], xmax=ordered_df[column2], color='grey', alpha=0.4)
plt.scatter(ordered_df[column1], my_range, color='tab:blue', alpha=1, label=column1)
# plt.scatter(ordered_df[column1], my_range, color='skyblue', alpha=1, label=column1)
plt.scatter(ordered_df[column2], my_range, color='tab:orange', alpha=1, label=column2)
# plt.scatter(ordered_df[column2], my_range, color='green', alpha=1, label=column2)
# plt.scatter(ordered_df['value2'], my_range, color='green', alpha=0.4 , label='value2')
plt.legend(loc='lower right')

plt.yticks(my_range, ordered_df['name'])
# plt.title("Comparison of the value 1 and the value 2", loc='left')
plt.xlabel('Reads Per Million (RPM)')
plt.ylabel('codons')

# plt.show()

figure = plt.gcf()

figure.set_size_inches(15, 10)
plt.savefig(image_path, dpi=300)


exit()

