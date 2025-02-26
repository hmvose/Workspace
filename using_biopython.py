from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

#initialize a Sequence Object (inherently read-only):
my_seq = Seq("ACGTTGCAAAA")

#can have helper functions for complement and reverse complement, functions similarly to python strings
# print(my_seq.complement())
# print(my_seq.reverse_complement())

#can parse/output fasta
# for seq_record in SeqIO.parse("lily_orchids.fasta", "fasta"):
#     print(seq_record.id)
#     print(repr(seq_record.seq))
#     print(len(seq_record))
# fasta_format = ">Name\n%s\n" % my_seq
# print(fasta_format)

#can parse GenBank
# for seq_record in SeqIO.parse("lily_orchids.gbk", "genbank"):
#     print(seq_record.id)
#     print(repr(seq_record.seq))
#     print(len(seq_record))

#able to pull directly from Entrez/NCBI, ExPASy, and SCOP

#can calculate GC content
#print(gc_fraction(my_seq))

#can transcribe DNA to RNA using .transcribe(), and vice versa using .back_transcribe()

