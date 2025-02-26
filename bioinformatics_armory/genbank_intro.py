from Bio import Entrez
import libraries.user_funcs as uf

db_info = uf.get_file("rosalind_gbk.txt").readlines()
#db_info = ["Anthoxanthum", "2003/7/25", "2005/12/27"]

search_term = '"%s"[Organism] AND (%s:%s[dp])' % (db_info[0], db_info[1], db_info[2])
print(search_term)

Entrez.email = "hmvose@gmail.com"
handle = Entrez.esearch(db="nucleotide", term=search_term)
record = Entrez.read(handle)
print(record["Count"])