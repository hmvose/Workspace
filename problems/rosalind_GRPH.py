import libraries.user_funcs as uf

#put get_file here
fasta_list = uf.read_fasta("rosalind_grph.txt")

directed_dict = {}
curr_adjacencies = []

for strand in fasta_list:
    #print(strand)
    #print("now checking: " + strand.name)
    curr_name = strand.name
    curr_strand = strand.dna
    strand_length = len(curr_strand)
    for item in fasta_list:
        if (curr_strand[(strand_length-3):strand_length] == item.dna[0:3]) and (curr_name != item.name):
            curr_adjacencies.append(item.name)
    if curr_adjacencies != []:
        directed_dict[curr_name] = curr_adjacencies
        curr_adjacencies = []

for key, value in directed_dict.items():
    for adj in value:
        print(key + " " + adj)