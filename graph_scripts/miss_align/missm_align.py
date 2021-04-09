import sys
import matplotlib.pyplot as plt
import matplotlib
import os

args = sys.argv



print("This script will generate a plot (.png) for each file (.align) that it finds in the folder provided.")
print("Graphs are stored in the same folder. Previous plots with the same name will be OVERWRITTEN.")
print("Type 'y' and press ENTER if you know what you are doing :)")
answer = input()
if not answer.lower() == "y":
    exit()

folder_path = sys.argv[1]

files = [x for x in os.listdir(folder_path) if (os.path.isfile(os.path.join(folder_path,x)) and
(x.endswith(".align.txt") or x.endswith(".align")) and not x.startswith(".")) ]
for f in files:
    file_path = os.path.join(folder_path,f)
    print(file_path)
    # file_path = "Homo_sapiens_chr6.trna132-ValAAC tRNA.align.txt"
    file_base = ".".join(file_path.split(".")[:-1])
    file_name = file_base.split("/")[-1]


    count_dict = {}

    with open(file_path) as tfile:
        lines = tfile.readlines()

    x_axis = list(lines[0].split(" ")[0])

    # for line in lines[2:20]:
    for line in lines[2:]:
        # print(line.split("\t")[-3].split("(")[0])
        seq = line.split("\t")[-4]
        c = int(line.split("\t")[-3].split("(")[0].replace(",",""))
        # print(seq,c)
        if not count_dict.get(seq):
            count_dict[seq] = c
        else:
            count_dict[seq] = count_dict[seq] + c


    # coverage per position
    zero_list = [0] * len(x_axis)
    mm_A = [0] * len(x_axis)
    mm_C = [0] * len(x_axis)
    mm_T = [0] * len(x_axis)
    mm_G = [0] * len(x_axis)

    for sequence in count_dict.keys():
        count = count_dict[sequence]
        # print(count)
        for ix,letter in enumerate(sequence):
            try:
                if not letter == " ":
                    zero_list[ix] = zero_list[ix] + count
                    if not letter == x_axis[ix]:
                        if letter=="A":
                            mm_A[ix] = mm_A[ix] + count
                        if letter=="C":
                            mm_C[ix] = mm_C[ix] + count
                        if letter=="T":
                            mm_T[ix] = mm_T[ix] + count
                        if letter=="G":
                            mm_G[ix] = mm_G[ix] + count
            except:
                pass


    labels = x_axis
    labels_x = [i for i in range(len(labels))]
    width = 0.5
    fig, ax = plt.subplots()
    ax.bar(labels_x, mm_A, width, label='A')
    ax.bar(labels_x, mm_C, width, label='C')
    ax.bar(labels_x, mm_T, width, label='T')
    ax.bar(labels_x, mm_G, width, label='G')

    plt.xticks(labels_x, labels)
    ax.legend()


    ax2 = ax.twinx()
    top_tick = 1.05 * max(zero_list)
    plt.ylim(bottom=0, top=top_tick)
    ax2.set_ylim(0, top_tick )
    ax.set_ylim(0, top_tick )
    ax2.plot(ax.get_xticks(), zero_list , linestyle='-',
            color='k', linewidth=1.0)
    # plt.ylim(bottom=0,top=max(count_dict.values()))
    # plt.setp(ax, ylim=[0,max(count_dict.values())])
    
    # plt.show()
    # plt.tick_params(axis='x', which='major', labelsize=100)
    # plt.tight_layout()

    # fig.set_size_inches(18.5, 10.5)
    plt.title(file_name)
    fig.set_size_inches(18.5, 10.5)
    plt.savefig(file_base + ".png")

print("")
print("Finished plotting!")

