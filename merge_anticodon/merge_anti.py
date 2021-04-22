import sys
import os

args = sys.argv

# Homo_sapiens_chr1.trna108-AsnGTT:tRNA.align

folder_path = sys.argv[1]
# folder_path = "/Users/ernesto/PycharmProjects/tRNA_is_life/merge_aligns/HL5_ctrl_tRNA Ser probe alignment"
# folder_path = "/Users/ernesto/Desktop/colabo/Chantal/tRNA_is_life/data/GRCh38_p10_genomic_tRNA"
merged_path = os.path.join(folder_path,"anticodon_align")

files = [x for x in os.listdir(folder_path) if (os.path.isfile(os.path.join(folder_path,x)) and x.endswith(".align"))]

anti_dict = {}

def merge_aligns(out_path,file_list):
    seq_dict = {}
    references = []
    lengths = []

    for f in file_list:
        file_path = os.path.join(folder_path, f)
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
            c = int(line.split("\t")[-3].split("(")[0].replace(",", ""))
            # print(seq,c)
            if not seq_dict.get(seq):
                seq_dict[seq] = c
            else:
                seq_dict[seq] = seq_dict[seq] + c

    #     print(f)
    #     print(len(seq_dict.keys()), sum(seq_dict.values()))
    #
    # print(len(set(references)))
    # print(len(files))
    # print(lengths)

    with open(os.path.join(out_path), "w") as wf:
        wf.write(references[0] + "\n")
        wf.write(references[0] + "\n")
        for k in seq_dict.keys():
            wf.write(k + "\t" + str(seq_dict[k]) + "(" + "\t\t\n")

if not(os.path.exists(merged_path)):
    os.mkdir(merged_path)

for f in files:
    chunks = f.split(":")[0]
    chunk = chunks.split("-")[1]
    if anti_dict.get(chunk):
        anti_dict[chunk] = anti_dict[chunk] + [f]
    else:
        anti_dict[chunk] = [f]
    # print(chunk)
c = 0
for x,y in anti_dict.items():
    c = c+1
    file_path = os.path.join(merged_path,x+".align")
    merge_aligns(file_path,y)
    print("merged " + x)
    print(str(c) + "/" + str(len(anti_dict)))
# print(anti_dict)







