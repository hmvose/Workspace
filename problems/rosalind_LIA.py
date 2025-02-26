import libraries.user_funcs as uf
import math
from scipy import stats as st

k, n = uf.str_to_nums(uf.get_file("rosalind_lia.txt").readline())

#k,n = [2,1]

#final_prob = 1 - st.binom.cdf(n-1, 2**k, 0.25) #good lord this is SO SLOW (i should be using R realistically)

for i in range(n, 2**k + 1):
    final_prob = final_prob + math.comb(2**k, i) * (0.25**i) * (0.75**((2**k)-i))
                                                            
print(final_prob)

#for R: pbinom(n-1, 2^k, 0.25, lower.tail = F)
#this is a BINOMIAL distribution: successes vs failures (either a child is heterozygous for both alleles or they aren't)