from Bio.Seq import Seq
import libraries.user_funcs as uf

sequence = Seq(uf.get_file("rosalind_ini.txt").readline())

counts = [sequence.count("A"), sequence.count("C"), sequence.count("G"), sequence.count("T")]

print(uf.list_to_str(counts, " "))

#the far more eloquent way:
# output = '%s %s %s %s' % (my_seq.count("A"),
#                           my_seq.count("C"),
#                           my_seq.count("G"),
#                           my_seq.count("T"))