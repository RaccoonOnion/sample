import sys
import networkx as nx
import time

# The main function
if __name__ == "__main__":

    # One input cmd line arguments
    input_file_path = sys.argv[1]

    # Extract file name
    arr = input_file_path.split('/')
    file_name = arr[-1]

    t1 = time.time()

	# Read graph from file
    E = []
    fr = open(input_file_path, 'r')
    for line in fr:
        if '%' in line: continue               # The first line in the file starts with '%'
        arr = line.rstrip().split()
        E.append((int(arr[0]), int(arr[1])))

    t1dot5 = time.time() 
    print(f"Reading Graph ends!! Time used is: {t1dot5-t1}s")

    G = nx.DiGraph()                           # Networkx directed graph
    G.add_edges_from(E)

    t2 = time.time()
    print(f'Adding edges from E to G finished! Time used is: {t2 - t1dot5}s')

	# Get in/out-degree sequences by calling functions in networkx and write the in/out-degree sequence to a file

    t3 = time.time()

    fw = open(f'original_degree_sequence.txt','w')
    ind_list = G.in_degree()
    outd_list = G.out_degree()
    for (node, ind) in ind_list:
        outd = outd_list[node]
        fw.write(f'{ind},{outd}\n')
    fw.close()

    t3dot5 = time.time()
    print(f'Getting and writing in/out-degree sequences by neworkx functions finished. Time cost is {t3dot5 - t3}s')
