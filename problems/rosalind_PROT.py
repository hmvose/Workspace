import libraries.user_funcs as uf
import math

rna_string = uf.get_file("rosalind_prot.txt").readline()

rna_codons ={"UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V", "UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V",
             "UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V", "UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V",
             "UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A", "UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
             "UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A", "UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
             "UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D", "UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D",
             "UAA":"Stop", "CAA":"Q", "AAA":"K", "GAA":"E", "UAG":"Stop", "CAG":"Q", "AAG":"K", "GAG":"E",
             "UGU":"C", "CGU":"R", "AGU":"S", "GGU":"G", "UGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
             "UGA":"Stop", "CGA":"R", "AGA":"R", "GGA":"G", "UGG":"W", "CGG":"R", "AGG":"R", "GGG":"G"}

#rna_string = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
translated = []
curr_codon = ""
stop_chain = False
iter = 0

while stop_chain == False:
    curr_codon = rna_string[iter:iter+3]
    if rna_codons[curr_codon] == "Stop":
        stop_chain = True
    else:
        translated.append(rna_codons[curr_codon])
        iter = iter + 3

print("".join(translated))
