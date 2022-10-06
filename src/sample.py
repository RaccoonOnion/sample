'''
This is the test whether the algorithm can preserve the ind and outd distribution
'''
import sys
import networkx as nx
import numpy as np
import math
from scipy.sparse import dok_array
import random
from operator import itemgetter
import traceback
import time

def test(G,k,t):
	t3 = time.time()
	in_degrees = G.in_degree()
	out_degrees = G.out_degree()
	ind_max = 0
	outd_max = 0
	for (node, ind) in in_degrees:
		outd = out_degrees[node]
		if ind > ind_max: ind_max = ind
		if outd > outd_max: outd_max = outd
	t4 = time.time()
	print(f'ind_max is {ind_max}, outd_max is: {outd_max}, time cost is: {t4-t3}s')
	
	A = dok_array((outd_max+1, ind_max+1), dtype=np.intc)
	B = dok_array((outd_max+1, ind_max+1), dtype=np.intc)
	
	for (u, v) in G.edges:
		outd = G.out_degree(u)
		ind = G.in_degree(v)
		A[outd, ind] += 1
	
	for (node, ind) in in_degrees:
		outd = G.out_degree(node)
		B[outd, ind] += 1
	t5 = time.time()
	print(f"A, B finish. Time cost is {t5-t4}s")	
	# Sampling process
	A_s = dok_array((outd_max+1, ind_max+1), dtype=np.intc)
	B_s = dok_array((outd_max+1, ind_max+1), dtype=np.intc)	
	for (key, value) in A.items():
		outd = key[0]
		ind = key[1]
		A_s[outd, ind] += round(value*k)
	
	for (key, value) in B.items():
		outd = key[0]
		ind = key[1]
		B_s[outd, ind] += round(value*k)
	t6 = time.time()
	print(f"Sampling finish. Time cost is {t6-t5}s") #A_s is {A_s.toarray()}\n B_s is {B_s.toarray()}")
	
	SG = nx.MultiDiGraph()
	# for a given group, keep the list of all available node ids.
	degree_nodelist_in = {}
	degree_nodelist_out = {}
	# for a given node, keep track of the remaining stubs to be added.
	free_stubs_out = {}
	free_stubs_in = {}
	# keep track of non-chords between pairs of node ids.
	#non_chords = {}		
	
	idx = 1
	for (key, value) in B_s.items():
		outd = key[0]
		ind = key[1]
		id_list = []
		for i in range(value):
			id_list.append(idx)
			idx += 1
		if not ind == 0: 
			if ind in degree_nodelist_in.keys():
				degree_nodelist_in[ind].extend( id_list.copy() )
			else:
				degree_nodelist_in[ind] = id_list.copy()	
		if not outd == 0:
			if outd in degree_nodelist_out.keys():
				degree_nodelist_out[outd].extend( id_list.copy() )
			else:
				degree_nodelist_out[outd] = id_list.copy()
		for node in id_list:
			if not outd == 0: free_stubs_out[node] = outd
			if not ind == 0: free_stubs_in[node] = ind
	t7 = time.time()
	print(f'Initialization finishes! Time cost is {t7-t6}s') #in nodes are {degree_nodelist_in}\n out nodes are {degree_nodelist_out}\n')
	'''
	Notice that for now the selection of k and l are not ordered, instead they are arranged in the order of input!!!
	'''
	flag = True
	E = []
	for (key, value) in sorted(A_s.items(), key=itemgetter(1), reverse=True):
		if flag:
			flag = False
			t8 = time.time()
			print(f"Sorting finish! Time cost is: {t8-t7}s")
		#print(f'len of E is:{len(E)}')
		outd = key[0]
		ind = key[1]
		#print(f'ind is {ind}, outd is {outd}')
		if ind in degree_nodelist_in.keys():
			l_in = len(degree_nodelist_in[ind])
		else:
			continue

		if not outd in degree_nodelist_out.keys():
			continue
		#print(f'ind is {ind}, outd is {outd}')
		
		degree_nodelist_in_copy = degree_nodelist_in[ind].copy()
		for i in range(l_in):
			if len(degree_nodelist_in_copy) == 0 or len(degree_nodelist_out[outd]) == 0: break
			degree_nodelist_out_copy = degree_nodelist_out[outd].copy()
			l_out = len(degree_nodelist_out_copy)
			u = random.randrange(len(degree_nodelist_in_copy))
			id_in = degree_nodelist_in_copy.pop(u)
			#flag = 0
				
			# Add a lot of edges at a time
			in_stubs = free_stubs_in[id_in]
			if value < in_stubs and value < l_out:
				id_out_list = random.sample(degree_nodelist_out_copy, value)
				free_stubs_in[id_in] -= value
				value = 0
			elif value < in_stubs and value >= l_out:
				#flag = 1
				id_out_list = degree_nodelist_out_copy
				free_stubs_in[id_in] -= l_out
				value -= l_out
			elif value >= in_stubs and value < l_out:
				#flag = 2
				id_out_list = random.sample(degree_nodelist_out_copy, in_stubs)
				del free_stubs_in[id_in]
				degree_nodelist_in[ind].remove(id_in)
				value -= in_stubs
			elif value >= in_stubs and value >= l_out:
				if in_stubs > l_out:
					#flag = 3
					id_out_list = degree_nodelist_out_copy
					free_stubs_in[id_in] -= l_out
					value -= l_out
				elif in_stubs < l_out:
					#flag = 4
					id_out_list = random.sample(degree_nodelist_out_copy, in_stubs)
					del free_stubs_in[id_in]
					degree_nodelist_in[ind].remove(id_in)
					value -= in_stubs
				else:	
					#flag = 5
					id_out_list = degree_nodelist_out_copy
					del free_stubs_in[id_in]
					degree_nodelist_in[ind].remove(id_in)
					value -= l_out
			for id_out in id_out_list:
				E.append((id_out, id_in))
				if free_stubs_out[id_out] == 1:
					del free_stubs_out[id_out]
					degree_nodelist_out[outd].remove(id_out)
				else:
					free_stubs_out[id_out] -= 1
			if value == 0: break
	t9 = time.time()
	print(f'Edges generating finish! Time cost is {t9-t8}s')
	SG.add_edges_from(E)
	t10 = time.time()
	print(f'Adding edges finished, time cost is {t10 - t9}s')
	fw = open(f'sampled_{k}_degree.txt','w')
	sampled_in = SG.in_degree()
	sampled_out = SG.out_degree()
	for (node, ind) in sampled_in:
		outd = sampled_out[node]
		fw.write(f'{ind},{outd}\n')
	fw.close()
	t11 = time.time()
	print(f'Calculating and writing ind, outd finish! Time cost is {t11-t10}s')
	print(f'Total time cost is {t11-t}s')	

	nx.write_edgelist(SG, f"sampled_{k}_edge_list")
	t12 = time.time()
	print(f'Writing edges finished, time cost is {t12 - t11}s')
	SG_simple = nx.DiGraph()
	SG_simple.add_edges_from(E)
	simple_e = SG_simple.size()	
	tol_e = SG.size()
	t13 = time.time()
	print(f'Calculating multiple edges finish! Time cost is {t13 - t12}, difference is {tol_e - simple_e}')	

if __name__ == "__main__":
	t1 = time.time()
	E = []
	fr = open(sys.argv[1], 'r')
	for line in fr:
		if '%' in line: continue
		arr = line.rstrip().split()
		E.append((int(arr[0]), int(arr[1])))
	G = nx.DiGraph()
	G.add_edges_from(E)
	t2 = time.time()
	print(f"Reading Graph ends!! Time used is: {t2-t1}s")
	test(G, float(sys.argv[2]), t1)

