# Import curve fitting package from scipy and other dependencies
from scipy.optimize import curve_fit 
import numpy as np
import sys
# import read functions
import read

# "$FILE"_"$sample_ratio"_ind_distr.csv "$FILE" "$sample_ratio" ind
# cmd line args
path = sys.argv[1]
dataset_name = sys.argv[2]
dataset_type = sys.argv[3]
io_flag = sys.argv[4]


# Function to calculate the power-law with constants a and b
def power_law(x, a, b):
    return a*np.power(x, b)

# (ind_list, ind_fre_list) = read.read_vec_2('../results/out.librec-filmtrust-trust/out.librec-filmtrust-trust_original_ind-distr.csv', ',')
(deg_list, fre_list) = read.read_vec_2(path, ',')
# we need to get rid of the zero deg because that will cause error during fitting
deg_list_ad = deg_list[1:]
fre_list_ad = fre_list[1:]
# Fit the dummy power-law data
pars, cov = curve_fit(f=power_law, xdata=deg_list_ad, ydata=fre_list_ad, p0=[0, 0], bounds=(-np.inf, np.inf))
# Get the standard deviations of the parameters (square roots of the # diagonal of the covariance)
stdevs = np.sqrt(np.diag(cov))
# Calculate the residuals
# res = fre_list_ad - power_law(deg_list_ad, *pars)
print(f'Dataset: {dataset_name}, dataset type: {dataset_type}, {io_flag}')
print(f'Results: a={pars[0]}, b={pars[1]}; stdev of a: {stdevs[0]}, stdev of b: {stdevs[1]}\n')