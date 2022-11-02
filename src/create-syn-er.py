import networkx as nx

'''
ER random graph, complexity: O(n^2)
'''
# er = nx.erdos_renyi_graph(10000, 1e-5,directed=True)
# print("er finished.")

'''
Fast implementation of ER random graph for small p
This algorithm runs in O(n+m) time, where m is the expected number of edges, 
which equals pn(n-1)/2
'''
for i in range(5):
    er_fast = nx.fast_gnp_random_graph(100000, 1e-5,directed=True)
    nx.write_edgelist(er_fast, f"../data/synthetic/er{i}", data=False)
    print(f"er{i} fast finished")






