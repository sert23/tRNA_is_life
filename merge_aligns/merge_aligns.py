import sys
import os

args = sys.argv

# folder_path = sys.argv[1]
folder_path = "/Users/ernesto/PycharmProjects/tRNA_is_life/merge_aligns/HL5_ctrl_tRNA Ser probe alignment"

files = [x for x in os.listdir(folder_path) if (os.path.isfile(os.path.join(folder_path,x)) and x.endswith(".align"))]

if "merged.align" in files:
    files.remove("merged.align")


seq_dict = {}
references = []
lengths = []

for f in files:
    file_path = os.path.join(folder_path,f)
    with open(file_path) as tfile:
        lines = tfile.readlines()

    x_axis = list(lines[0].split(" ")[0])
    x = lines[0].split(" ")[0]
    lengths.append(len(x))
    references.append(x)
    # for line in lines[2:20]:
    for line in lines[2:]:
        # print(line.split("\t")[-3].split("(")[0])
        seq = line.split("\t")[-4]
        c = int(line.split("\t")[-3].split("(")[0].replace(",",""))
        # print(seq,c)
        if not seq_dict.get(seq):
            seq_dict[seq] = c
        else:
            seq_dict[seq] = seq_dict[seq] + c

    print(f)
    print(len(seq_dict.keys()), sum(seq_dict.values()))

print(len(set(references)))
print(len(files))
print(lengths)


with open(os.path.join(folder_path, "merged.align"),"w") as wf:
    wf.write(references[0] +"\n")
    wf.write(references[0] +"\n")
    for k in seq_dict.keys():
        wf.write(k+"\t" + str(seq_dict[k])  + "(" + "\t\t\n")




