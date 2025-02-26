from libraries import user_funcs as uf

dna_seqs = uf.get_file("rosalind_hamm.txt").readlines()

mismatch = 0
for i in range(len(dna_seqs[0])):
    if dna_seqs[0][i] != dna_seqs[1][i]:
        mismatch = mismatch + 1

print(mismatch)