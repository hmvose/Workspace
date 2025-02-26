import libraries.user_funcs as uf

node_list = uf.get_file("rosalind_tree.txt").readlines()
parsable_nodes = []
num_nodes = int(node_list[0].replace("\n", ""))
node_list.pop(0)

for node in node_list:
    cleaned = node.replace("\n", "")
    parsable_nodes.append(uf.str_to_nums(node))

print(num_nodes - 1 - len(node_list))