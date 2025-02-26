import libraries.user_funcs as uf

fasta_list = uf.read_fasta("rosalind_lcsm.txt")
#print(fasta_list)

def lcs_generator(strand: str) -> list:
    lcs_list = []
    for i in range(len(strand)):
        for j in range(len(strand)):
            lcs_list.append(strand[i:j+1])
    lcs_list = list(set(lcs_list))
    lcs_list.sort(key=len)
    return lcs_list[::-1]


shortest_dna = "o" * 9999

for strand in fasta_list:
    if len(strand.dna) <= len(shortest_dna):
        shortest_dna = strand.dna
        to_remove = strand
    
fasta_list.remove(to_remove)

all_possible_lcs = lcs_generator(shortest_dna)

#print(all_possible_lcs)
found_lcs = False

for lcs in all_possible_lcs:
    found_lcs = True
    for dna in fasta_list:
        if lcs not in dna.dna:
            found_lcs = False
            break
    if found_lcs == True:
        final_lcs = lcs
        break

print(final_lcs)
