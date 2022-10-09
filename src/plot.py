import matplotlib.pyplot as plt
import numpy as np
import sys
import time

# The main function
if __name__ == "__main__":

    # Two input cmd line arguments
    folder_path = sys.argv[1]
    dataset_name = sys.argv[2]
    sample_ratio = sys.argv[3]

    t1 = time.time()

	# Read in/out-degree distributions from file
    fig, axs = plt.subplots(2, 2, sharex='col')
    font = {
        'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 10,
        }
    # Read and plot sampled in-degree distribution
    x_in_sam, y_in_sam = ([] for i in range(2))
    fr = open(folder_path + "/" + dataset_name + "_" + sample_ratio + "_ind-distr.csv", 'r')
    for line in fr:
        if '%' in line: continue               # The first line in the file starts with '%'
        arr = line.rstrip().split(',')
        x_in_sam.append(int(arr[0]))
        y_in_sam.append(int(arr[1]))
    axs[0, 0].scatter(x_in_sam, y_in_sam, marker=".")
    axs[0, 0].set_yscale('log')
    axs[0, 0].set_xscale('log')
    # axs[0, 0].loglog(x_in_sam, y_in_sam, nonpositive = 'mask', base = 10)
    axs[0, 0].set_title('Sampled in-degree distribution', fontdict = font)

    # Read and plot sampled out-degree distribution
    x_out_sam, y_out_sam = ([] for i in range(2))
    fr = open(folder_path + "/" + dataset_name+"_"+sample_ratio+"_outd-distr.csv", 'r')
    for line in fr:
        if '%' in line: continue               # The first line in the file starts with '%'
        arr = line.rstrip().split(',')
        x_out_sam.append(int(arr[0]))
        y_out_sam.append(int(arr[1]))
    axs[0, 1].scatter(x_out_sam, y_out_sam, marker=".")
    axs[0, 1].set_yscale('log')
    axs[0, 1].set_xscale('log')
    # axs[0, 1].loglog(x_out_sam, y_out_sam, nonpositive = 'mask', base = 10)
    axs[0, 1].set_title('Sampled out-degree distribution', fontdict = font)

    # Read and plot original in-degree distribution
    x_in_origin, y_in_origin = ([] for i in range(2))
    fr = open(folder_path + "/" + dataset_name+"_"+"original"+"_ind-distr.csv", 'r')
    for line in fr:
        if '%' in line: continue               # The first line in the file starts with '%'
        arr = line.rstrip().split(',')
        x_in_origin.append(int(arr[0]))
        y_in_origin.append(int(arr[1]))
    axs[1, 0].scatter(x_in_origin, y_in_origin, marker=".")
    axs[1, 0].set_yscale('log')
    axs[1, 0].set_xscale('log')
    # axs[1, 0].loglog(x_in_origin, y_in_origin, nonpositive = 'mask', base = 10)  
    axs[1, 0].set_title('Original in-degree distribution', fontdict = font)

    # Read and plot original out-degree distribution
    x_out_origin, y_out_origin = ([] for i in range(2))
    fr = open(folder_path + "/" + dataset_name+"_"+"original"+"_outd-distr.csv", 'r')
    for line in fr:
        if '%' in line: continue               # The first line in the file starts with '%'
        arr = line.rstrip().split(',')
        x_out_origin.append(int(arr[0]))
        y_out_origin.append(int(arr[1]))
    axs[1, 1].scatter(x_out_origin, y_out_origin, marker=".")
    axs[1, 1].set_yscale('log')
    axs[1, 1].set_xscale('log')
    # axs[1, 1].loglog(x_out_origin, y_out_origin, nonpositive = 'mask', base = 10)  
    axs[1, 1].set_title('Original out-degree distribution', fontdict = font)

    t1dot5 = time.time() 
    print(f"Reading and ploting Distributions ends!! Time used is: {t1dot5-t1}s")

    fig.savefig("scatter_"+dataset_name+"_log"+".png", transparent=False, dpi=800, bbox_inches="tight")

    print(f'Plotting finished for dataset {dataset_name}!')


