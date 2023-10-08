from sample import *
from utils import *
from functions import *
from numpy import std
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import math

sample_size = int(input('Sample size: '))
number_of_samples = int(input('Number of samples to be generated: '))

data = sort_into_categories(find_sample_collection(sample_size, number_of_samples, linear)[0])

x = np.arange(1, len(data) + 1)
y = np.array(data)

# Create x and y arrays from the given data
x = np.arange(1, len(data) + 1)
y = np.array(data)

# Define the Gaussian function for the line of best fit
def gaussian_fit(x, m, s):
    return 1 / (s * math.sqrt(2 * math.pi)) * np.exp(-1 / 2 * ((x - m) / s)**2)

# Fit the data to the Gaussian function
params, _ = curve_fit(gaussian_fit, x, y)

# Extract the fitted parameters
m, s = params

# Generate the predicted y values for the line of best fit
y_fit = gaussian_fit(x, m, s)

# Create the matplotlib plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Data')
plt.plot(x, y_fit, label=f'Line of Best Fit: Gaussian', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data and Line of Best Fit (Gaussian)')
plt.legend()
plt.grid(True)
plt.show()
