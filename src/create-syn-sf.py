import networkx as nx

for i in range(5):
    sf = nx.scale_free_graph(100000)
    nx.write_edgelist(sf, f"../data/synthetic/sf{i}", data=False)
    print(f"sf{i} finished")
