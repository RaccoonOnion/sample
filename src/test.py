import sample
import time
import sys
import networkx as nx

'''
The main function
Inputs: input_file_path: edge list file, input_sample_ratio: sample ratio
Outputs: in/out-degree sequence file, edge list file, statistics.txt: time statistics 
'''
if __name__ == "__main__":

    # Two input cmd line arguments
    input_file_path = sys.argv[1]
    arr = input_file_path.split('/')
    file_name = arr[2]
    input_sample_ratio = float(sys.argv[2])
    
    time_list = []

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
    time_list.append(t1dot5-t1)

    G = nx.DiGraph()                           # Networkx directed graph
    G.add_edges_from(E)

    t2 = time.time()
    print(f'Adding edges from E to G finished! Time used is: {t2 - t1dot5}s')
    time_list.append(t2 - t1dot5)

    # Calling the sample function
    result = sample.sample(G, input_sample_ratio, file_name)
    time_list.extend(result[0])
    multi_edge_number = result[1]

    fw = open("results/" + file_name + "/statistics.txt",'w')
    for time in time_list:
        fw.write(f'{str(time)}\n')
    fw.write(f'# multi-edges: {str(multi_edge_number)}')
    fw.close()
