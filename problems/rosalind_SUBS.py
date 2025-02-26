import libraries.user_funcs as uf

dna_string, substring = uf.get_file("rosalind_subs.txt").readlines()

dna_string = dna_string.replace("\n", "")
substring = substring.replace("\n", "")

#dna_string, substring = ["GATATATGCATATACTT", "ATAT"]

locations = []
potential_match = False

for i in range(len(dna_string)):
    
    if dna_string[i] == substring[0]:
        for j in range(1, len(substring)):
            if i+j >= len(dna_string):
                potential_match = False
                break
            elif dna_string[i+j] != substring[j]:
                potential_match = False
                break
            else:
                potential_match = True
            
        if potential_match == True:
            locations.append(i+1)
            potential_match = False

indices = uf.list_to_str(locations, " ")

print(indices)
            
        