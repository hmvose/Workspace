import math
import libraries.user_funcs as uf


file_obj = uf.get_file("rosalind_fibd.txt").readline()

months, lifespan = uf.str_to_nums(file_obj)

#months, lifespan = [6,3]

babies = 1
repro = 0
dying = [0]*(lifespan-1)
dying.append(1)
print(dying)

for i in range(0, months):
    print("BEGINNING MONTH " + str(i+1))
    print("dying array: " + (" ".join(str(nums) for nums in dying)))
    print("babies: " + str(babies))
    print("repro: " + str(repro))
    print("total rabbits: " + str(babies+repro))
    if i != 0:
        dying.append(new_babies)
    new_babies = repro
    repro = repro - dying[0] + babies
    babies = new_babies
    del dying[0]

print(babies+repro)
