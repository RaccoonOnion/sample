import read
import sys
import numpy as np

# cmd line args
path = sys.argv[1]
dataset_name = sys.argv[2]
dataset_type = sys.argv[3]
io_flag = sys.argv[4]

(deg_list, fre_list) = read.read_vec_2(path, ',')
N = sum(fre_list)
fre_list_np = np.array(fre_list)
fre_list_ad = (fre_list_np / N).tolist()

fw = open(f'../results/{dataset_name}/{dataset_name}_{dataset_type}_{io_flag}_fre-distr.csv','w')
length = len(deg_list)
for i in range(length):
    fw.write(str(deg_list[i])+','+str(fre_list_ad[i])+'\n')
fw.close()

