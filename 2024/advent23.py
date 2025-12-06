import timeit

from itertools import product
import networkx as nx

def p1(lines):
    connected_nodes = {}
    for line in lines:
        node1,node2 = line.split("-")
        if node1 not in connected_nodes:
            connected_nodes[node1] = set()
        if node2 not in connected_nodes:
            connected_nodes[node2] = set()
        connected_nodes[node1].add(node2)
        connected_nodes[node2].add(node1)
    
    sets_of_3 = set()
    for node1, connected_node_set in connected_nodes.items():
        if node1.startswith("t"):
            for node2 in connected_node_set:
                node3s = connected_node_set.intersection(connected_nodes[node2])
                for node3 in node3s:
                    sets_of_3.add(tuple(sorted([node1,node2,node3])))
                

    return len(sets_of_3)


def p2(lines):
    G = nx.Graph()

    for line in lines:
        node1,node2 = line.split("-")
        if node1 not in G:
            G.add_node(node1)
        if node2 not in G:
            G.add_node(node2)
        G.add_edge(node1,node2)


    gen_cliques = nx.enumerate_all_cliques(G)
    cliques_of_3_with_t = []
    for clique in gen_cliques:
        if len(clique) <3: continue
        if len(clique) >3: break
        if any([node.startswith("t") for node in clique]):
            cliques_of_3_with_t.append(clique)

    print (f"Part 1: {len(cliques_of_3_with_t)}")
    stop = timeit.default_timer()
    print(f'Time: {(stop - start):.4}')

    nodes, weight = nx.max_weight_clique(G,None)
    return "".join([node+"," for node in sorted(nodes)])[:-1]
    

f = open("input23.txt", "r")
lines = [line.strip() for line in f]
  
# start = timeit.default_timer()
# print (f"Part 1: {p1(lines)}")
# stop = timeit.default_timer()
# print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')