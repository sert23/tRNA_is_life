# launch like python3 make_correlation_plot.py corrs_fragments.xlsx
# check the example file to see the structure

import pandas as pd
import sys
import os
import seaborn as sns; sns.set_theme(color_codes=True)
import matplotlib.pyplot as plt
from scipy.stats import pearsonr



if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    # input_file = "/Users/ernesto/PycharmProjects/tRNA_is_life2/EV_paper/data/corrs_great60nt.xlsx"
    input_file = "/Users/ernesto/PycharmProjects/tRNA_is_life3/figures/3B/Figure3B.xlsx"


input_matrix = pd.read_excel(input_file, index_col=0)

columns = list(input_matrix.columns)

comparisons = []
for x in range(0, len(columns), 2):
    comparisons.append([columns[x], columns[x+1]])


folder_path = input_file.replace(".xlsx","") + "_labeled"
if not os.path.exists(folder_path):
    os.mkdir(folder_path)


# fig, ax = plt.subplots(figsize=(20, 10))

for comparison in comparisons:
    subset = input_matrix[comparison]
    comparison_string = comparison[0].replace(" ", "_") + "_vs_" + comparison[1].replace(" ", "_")
    comparison_string = comparison_string.replace("/", "-")
    output_file = os.path.join(folder_path,comparison_string + "_unlabeled.jpg")
    # ax, fig = sns.lmplot(x=comparison[0], y=comparison[1], data=subset)
    # fig = plt.figure()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax = sns.regplot(x=comparison[0], y=comparison[1], data=subset)
    # ax, fig = sns.lmplot
    r, pval = pearsonr(subset[comparison[0]].values, subset[comparison[1]].values)
    ax.text(0.1, 0.90, r'Pearson correlation (r): {} p-val={}'.format(str(round(r, 2)), str(round(pval, 10))), fontsize=15, transform = ax.transAxes)
    ax.set_xlabel(comparison[0].replace(".1", "") + " (RPM)")
    ax.set_ylabel(comparison[1].replace(".1", "") + " (RPM)")
    # ax.text(0.1, 0.90, r'Spearman correlation: $E=mc^2$', fontsize=15, transform = ax.transAxes)
    fig.savefig(output_file, dpi=600)

# exit()

folder_path = input_file.replace(".xlsx","") + "_labeled"
if not os.path.exists(folder_path):
    os.mkdir(folder_path)

for comparison in comparisons:
    subset = input_matrix[comparison]
    comparison_string = comparison[0].replace(" ", "_") + "_vs_" + comparison[1].replace(" ", "_")
    comparison_string = comparison_string.replace("/", "-")
    output_file = os.path.join(folder_path,comparison_string + "_labeled.jpg")
    # ax, fig = sns.lmplot(x=comparison[0], y=comparison[1], data=subset)
    # fig = plt.figure()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax = sns.regplot(x=comparison[0], y=comparison[1], data=subset)
    # ax, fig = sns.lmplot
    r, pval = pearsonr(subset[comparison[0]].values, subset[comparison[1]].values)
    # ax.text(0.1, 0.90, r'r = '+ str(round(r, 2)), fontsize=15, transform = ax.transAxes)
    ax.text(0.1, 0.90, r'Pearson correlation (r): {} p-val={}'.format(str(round(r, 2)), str(round(pval, 10))), fontsize=15, transform = ax.transAxes)
    ax.set_xlabel(comparison[0].replace(".1", "") + " (RPM)")
    ax.set_ylabel(comparison[1].replace(".1", "") + " (RPM)")
    for line in range(0, subset.shape[0]):
        ax.text(subset[comparison[0]].values[line] + 0.01, subset[comparison[1]].values[line], subset[comparison[0]].index[line] ,
                horizontalalignment='left',
                 color='black', fontsize=8)
    # ax.text(0.1, 0.90, r'Spearman correlation: $E=mc^2$', fontsize=15, transform = ax.transAxes)
    fig.savefig(output_file, dpi=600)

for comparison in comparisons:
    subset = input_matrix[comparison]
    comparison_string = comparison[0].replace(" ", "_") + "_vs_" + comparison[1].replace(" ", "_")
    comparison_string = comparison_string.replace("/", "-")
    output_file = os.path.join(folder_path,comparison_string + "_no_title.jpg")
    # ax, fig = sns.lmplot(x=comparison[0], y=comparison[1], data=subset)
    # fig = plt.figure()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax = sns.regplot(x=comparison[0], y=comparison[1], data=subset)
    # ax, fig = sns.lmplot
    r, pval = pearsonr(subset[comparison[0]].values, subset[comparison[1]].values)
    # ax.text(0.1, 0.90, r'r = '+ str(round(r, 2)), fontsize=15, transform = ax.transAxes)
    # ax.text(0.1, 0.90, r'Pearson correlation (r): {} p-val={}'.format(str(round(r, 2)), str(round(pval, 10))), fontsize=15, transform = ax.transAxes)
    ax.set_xlabel(comparison[0].replace(".1", "") + " (RPM)")
    ax.set_ylabel(comparison[1].replace(".1", "") + " (RPM)")
    # for line in range(0, subset.shape[0]):
    #     ax.text(subset[comparison[0]].values[line] + 0.01, subset[comparison[1]].values[line], subset[comparison[0]].index[line] ,
    #             horizontalalignment='left',
    #              color='black', fontsize=8)
    # ax.text(0.1, 0.90, r'Spearman correlation: $E=mc^2$', fontsize=15, transform = ax.transAxes)
    fig.savefig(output_file, dpi=600)