# Import curve fitting package from scipy and other dependencies
from scipy.optimize import curve_fit 
import numpy as np
import sys
# import read functions
import read

# Function to calculate the power-law with constants a and b
def power_law(x, a, b):
    return a*np.power(x, b)

# (ind_list, ind_fre_list) = read.read_vec_2('../results/out.librec-filmtrust-trust/out.librec-filmtrust-trust_original_ind-distr.csv', ',')
(ind_list, ind_fre_list) = read.read_vec_2('../results/out.librec-filmtrust-trust/out.librec-filmtrust-trust_0.75_ind-distr.csv', ',')
# we need to get rid of the zero deg because that will cause error during fitting
ind_list_ad = ind_list[1:]
ind_fre_list_ad = ind_fre_list[1:]
# Fit the dummy power-law data
pars, cov = curve_fit(f=power_law, xdata=ind_list_ad, ydata=ind_fre_list_ad, p0=[0, 0], bounds=(-np.inf, np.inf))
# Get the standard deviations of the parameters (square roots of the # diagonal of the covariance)
stdevs = np.sqrt(np.diag(cov))
# Calculate the residuals
res = ind_fre_list_ad - power_law(ind_list_ad, *pars)
print(pars[0], pars[1])
print(stdevs)