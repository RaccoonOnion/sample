import sys
import networkx as nx
import numpy as np
import math
from scipy.sparse import dok_array
import random
from operator import itemgetter
import traceback
import time


# Edge creation with A
def create_edges(ind2id_list, outd2id_list, id2freestubs_in, id2freestubs_out, A_s):

	t7 = time.time()

	flag = True    # Boolean Flag var indicating the first round of the loop
	E = []         # The edge set

	# Sort A_s with the sorting algorithm defaulted by python sorted() function
	# We use this process because by connecting the edges in descending order of value of A_s, we can minimize the loss
	for (key, value) in sorted(A_s.items(), key=itemgetter(1), reverse=True):

		# Record the time used for sorting
		if flag:
			flag = False
			t8 = time.time()
			print(f"Sorting of A_s finished! Time cost is: {t8-t7}s")

		# Check if there are still available nodes with pattern (outd, ind)
		outd = key[0]
		ind = key[1]
		#print(f'ind is {ind}, outd is {outd}')
		if ind in ind2id_list.keys():
			l_in = len(ind2id_list[ind])
		else:
			continue

		if not outd in outd2id_list.keys():
			continue
		
		# Add edges when possible
		degree_nodelist_in_copy = ind2id_list[ind].copy()
		for i in range(l_in):
			if len(degree_nodelist_in_copy) == 0 or len(outd2id_list[outd]) == 0: break
			degree_nodelist_out_copy = outd2id_list[outd].copy()
			l_out = len(degree_nodelist_out_copy)
			u = random.randrange(len(degree_nodelist_in_copy))
			id_in = degree_nodelist_in_copy.pop(u)
				
			# Add a lot of edges at a time
			in_stubs = id2freestubs_in[id_in]
			if value < in_stubs and value < l_out:
				id_out_list = random.sample(degree_nodelist_out_copy, value)
				id2freestubs_in[id_in] -= value
				value = 0
			elif value < in_stubs and value >= l_out:
				#flag = 1
				id_out_list = degree_nodelist_out_copy
				id2freestubs_in[id_in] -= l_out
				value -= l_out
			elif value >= in_stubs and value < l_out:
				#flag = 2
				id_out_list = random.sample(degree_nodelist_out_copy, in_stubs)
				del id2freestubs_in[id_in]
				ind2id_list[ind].remove(id_in)
				value -= in_stubs
			elif value >= in_stubs and value >= l_out:
				if in_stubs > l_out:
					#flag = 3
					id_out_list = degree_nodelist_out_copy
					id2freestubs_in[id_in] -= l_out
					value -= l_out
				elif in_stubs < l_out:
					#flag = 4
					id_out_list = random.sample(degree_nodelist_out_copy, in_stubs)
					del id2freestubs_in[id_in]
					ind2id_list[ind].remove(id_in)
					value -= in_stubs
				else:	
					#flag = 5
					id_out_list = degree_nodelist_out_copy
					del id2freestubs_in[id_in]
					ind2id_list[ind].remove(id_in)
					value -= l_out
			for id_out in id_out_list:
				E.append((id_out, id_in))
				if id2freestubs_out[id_out] == 1:
					del id2freestubs_out[id_out]
					outd2id_list[outd].remove(id_out)
				else:
					id2freestubs_out[id_out] -= 1
			if value == 0: break
	
	t9 = time.time()
	print(f'Edges generating finished! Time cost is {t9-t8}s')
	
	return E
	

'''
The sampling function:
Inputs:  G: The original graph, type is nx.DiGraph; k: input_sample_ratio, float (0,1)
Outputs: None
'''
def sample(G,k):

	t3 = time.time()

	# Get in/out-degree sequences by calling functions in networkx
	in_degrees = G.in_degree()
	out_degrees = G.out_degree()

	t3dot5 = time.time()
	print(f'Getting in/out-degree sequences by neworkx functions finished. Time cost is {t3dot5 - t3}s')

	# Find the maximum in/out-degree by looping the in-degree sequence
	ind_max = 0
	outd_max = 0
	for (node, ind) in in_degrees:
		outd = out_degrees[node]
		if ind > ind_max: ind_max = ind
		if outd > outd_max: outd_max = outd
	
	t4 = time.time()
	print(f'Getting max values finished! \nind_max is {ind_max}, outd_max is: {outd_max}, time cost is: {t4-t3dot5}s')

	# Create two dictionary-of-keys scipy sparse 2D arrays to store the matrices A and B
	# A is the Joint Degree Matrix (JDM)
	# B is the Degree Correlation Matrix (DCM)
	A = dok_array((outd_max+1, ind_max+1), dtype=np.intc)
	B = dok_array((outd_max+1, ind_max+1), dtype=np.intc)
	# Calculate A
	for (u, v) in G.edges:
		outd = G.out_degree(u)
		ind = G.in_degree(v)
		A[outd, ind] += 1
	# Calculate B
	for (node, ind) in in_degrees:
		outd = G.out_degree(node)
		B[outd, ind] += 1

	t5 = time.time()
	print(f"Initiating and calculating A, B finish. Time cost is {t5-t4}s")	

	# Sampling process

	# Create two dictionary-of-keys scipy sparse 2D arrays to store the sampled matrices A_s and B_s
	A_s = dok_array((outd_max+1, ind_max+1), dtype=np.intc)
	B_s = dok_array((outd_max+1, ind_max+1), dtype=np.intc)	
	# Sample A with k
	for (key, value) in A.items():
		outd = key[0]
		ind = key[1]
		A_s[outd, ind] += round(value*k)
	# Sample B with k
	for (key, value) in B.items():
		outd = key[0]
		ind = key[1]
		B_s[outd, ind] += round(value*k)

	t6 = time.time()
	print(f"Sampling A, B finished. Time cost is {t6-t5}s")
	
	# Constructing process

	# Create a networkx directed multi-graph SG to store the constucted graph
	SG = nx.MultiDiGraph()

	# for a given degree group, keep the list of all available node (with free stubs) ids.
	ind2id_list = {}
	outd2id_list = {}

	# for a given node, keep track of the remaining free stubs.
	id2freestubs_out = {}
	id2freestubs_in = {}

	# Using B to initiate degree_nodelist_in, degree_nodelist_out, free_stubs_out and free_stubs_in
	# We let the node id starts from 1
	id = 1
	for (key, value) in B_s.items(): # key is a tuple of shape (outd, ind), value is the number of nodes with (outd, ind) degree pattern
		outd = key[0]
		ind = key[1]
		id_list = []
		for i in range(value):
			id_list.append(id)
			id += 1
		if not ind == 0: 
			if ind in ind2id_list.keys():
				ind2id_list[ind].extend( id_list.copy() )
			else:
				ind2id_list[ind] = id_list.copy()	
		if not outd == 0:
			if outd in outd2id_list.keys():
				outd2id_list[outd].extend( id_list.copy() )
			else:
				outd2id_list[outd] = id_list.copy()
		for node in id_list:
			if not outd == 0: id2freestubs_out[node] = outd
			if not ind == 0: id2freestubs_in[node] = ind

	t7 = time.time()
	print(f'Graph Initialization with B_s finished! Time cost is {t7-t6}s')

	E = create_edges(ind2id_list, outd2id_list, id2freestubs_in, id2freestubs_out, A_s)

	t9 = time.time()
	# Add edges from E to SG
	SG.add_edges_from(E)

	t10 = time.time()
	print(f'Adding edges to SG and create graph finished, time cost is {t10 - t9}s')

	# write the in/out-degree sequence to a file
	fw = open(f'sampled_{k}_degree.txt','w')
	sampled_in = SG.in_degree()
	sampled_out = SG.out_degree()
	for (node, ind) in sampled_in:
		outd = sampled_out[node]
		fw.write(f'{ind},{outd}\n')
	fw.close()

	t11 = time.time()
	print(f'Calculating and writing ind, outd sequence finish! Time cost is {t11-t10}s')
	print(f'Total time cost for sampling function is {t11-t3}s')	

	# write edges to a file using networkx function .write_edgelist()
	nx.write_edgelist(SG, f"sampled_{k}_edge_list")

	t12 = time.time()
	print(f'Writing edges using nx finished, time cost is {t12 - t11}s')

	# Checking how many edges are multiple edges
	SG_simple = nx.DiGraph()
	SG_simple.add_edges_from(E)
	simple_e = SG_simple.size()	
	tol_e = SG.size()

	t13 = time.time()
	print(f'Calculating multiple edges finish! Time cost is {t13 - t12}, difference is {tol_e - simple_e}')	


# The main function
if __name__ == "__main__":

	# Two input cmd line arguments
	input_file_path = sys.argv[1]
	input_sample_ratio = float(sys.argv[2])

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
	

	# Calling the sample function
	sample(G, input_sample_ratio)


