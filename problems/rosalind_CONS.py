import math
import libraries.user_funcs as uf

fasta_list = uf.read_fasta("rosalind_cons.txt")


class ConsensusMatrix:

    def __init__(self, length: int):
        self.matrix = {
            "A":[0]*length, 
            "C":[0]*length, 
            "G":[0]*length, 
            "T":[0]*length,
            }

    def get_consensus_pair(self, index: int):
        highest_num = 0
        return_pair = ""
        if self.matrix["A"][index] > highest_num:
            return_pair = 'A'
            highest_num = self.matrix["A"][index]
        if self.matrix["C"][index] > highest_num:
            return_pair = 'C'
            highest_num = self.matrix["C"][index]
        if self.matrix["G"][index] > highest_num:
            return_pair = 'G'
            highest_num = self.matrix["G"][index]
        if self.matrix["T"][index] > highest_num:
            return_pair = 'T'
            highest_num = self.matrix["T"][index]
        
        return return_pair
    
    def get_consensus_str(self) -> str:
        consensus_build = []
        for i in range(len(self.matrix["A"])):
            consensus_build.append(self.get_consensus_pair(i))
        consensus_str = uf.list_to_str(consensus_build)

        return consensus_str
    
    def print_matrix(self):
        A_list = uf. list_to_str(self.matrix['A'], " ")
        C_list = uf. list_to_str(self.matrix['C'], " ")
        G_list = uf. list_to_str(self.matrix['G'], " ")
        T_list = uf. list_to_str(self.matrix['T'], " ")
        print(f"A: {A_list}")
        print(f"C: {C_list}")
        print(f"G: {G_list}")
        print(f"T: {T_list}")
        
        
new_cm = ConsensusMatrix(length=len(fasta_list[0].dna))

for fasta in fasta_list:
    for i in range(len(fasta.dna)):
        new_cm.matrix[fasta.dna[i]][i] = new_cm.matrix[fasta.dna[i]][i] + 1

print(new_cm.get_consensus_str())
new_cm.print_matrix()