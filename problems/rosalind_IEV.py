import libraries.user_funcs as uf

population = uf.get_file("rosalind_iev.txt").readline()
p1, p2, p3, p4, p5, p6 = uf.str_to_nums(population)

print(population)

prob1 = 1
prob2 = 1
prob3 = 1
prob4 = 0.75
prob5 = 0.5
prob6 = 0

#p1, p2, p3, p4, p5, p6 = [1,0,0,1,0,1]

expected_val = p1*2 + p2*2 + p3*2*prob3 + p4*2*prob4 + p5*2*prob5

print(expected_val)