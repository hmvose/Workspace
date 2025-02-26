import math

from libraries import user_funcs as uf
import problems.rosalind_HAMM as rosalind_HAMM

dna_info = uf.get_file('rosalind_gc').readlines()

dna_dict = {}
join_list = []
for i in range(len(dna_info)):
    dna_info[i] = dna_info[i].replace("\n","")
    if dna_info[i][0] == ">":
        keypair = i
        i = i+1
        while dna_info[i][0] != ">":
            dna_info[i] = dna_info[i].replace("\n","")
            join_list.append(dna_info[i])
            i = i+1
            if i >= len(dna_info):
                break
        valuepair = i-1
        i = i-1
        dna_dict[dna_info[keypair]] = "".join(join_list)
        join_list = []
        print("i at end: " + str(i))

highest_GC = 0
highest_GC_str = ""
for key, value in dna_dict.items():
    curr_gc = uf.GC_content(dna_dict[key])
    if curr_gc > highest_GC:
        highest_GC = curr_gc
        highest_GC_str = key

print(highest_GC_str.replace(">",""))
print(highest_GC * 100)
