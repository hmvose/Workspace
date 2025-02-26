from libraries import user_funcs as uf
import math

numbers = uf.get_file('rosalind_iprb.txt').readline()

k, m, n = list(uf.str_to_nums(numbers))

total_pop = k+m+n

#homozygous dominant: will always produce a dominant allele

homodom_total = (k/total_pop * (k-1)/(total_pop-1)) + (k/total_pop * m/(total_pop-1)) + (k/total_pop * n/(total_pop-1)) + (m/total_pop * k/(total_pop-1)) + (n/total_pop * k/(total_pop-1))

#heterozygous dominant: will produce dominant 75% of time if mated with hetero, 50% if recessive
test1 = (m/total_pop * n/(total_pop-1) * 0.5) + (n/total_pop * m/(total_pop-1)*0.5)
test2 = (m/total_pop * (m-1)/(total_pop-1) * 0.75)

final_prob = homodom_total + test1 + test2
print(final_prob)

#note: forgot to consider probability of ALL combinations, not just unique ones