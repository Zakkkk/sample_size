from sample import *
from utils import *
from functions import *
from numpy import std
import matplotlib.pyplot as plt
import numpy as np
import math

def find_collection_error(
        chosen_function, 
        sample_size, 
        number_of_samples, 
        plot_graph=False):
    
    test_collection = [chosen_function(x) for x in range(0,100)]
    test_collection_mean = find_mean(test_collection)
    test_collection_std_dev = std(test_collection)

    min_range = round(min(test_collection))
    max_range = round(max(test_collection))

    # print(f'min: {min_range}, max: {max_range}')

    sample_collection = find_sample_collection(sample_size, number_of_samples, chosen_function)
    sample_mean = sample_collection[1]
    sample_std_dev = sample_collection[2]
    data = sort_into_categories(sample_collection[0], min=min_range, max=max_range)

    x = np.arange(0, len(data))
    y = np.array(data)

    def expected_func(x):
        std_dev = test_collection_std_dev / math.sqrt(sample_size)
        return normal(x, test_collection_mean, std_dev) * number_of_samples

    std_error = percentage_error(y, expected_func, number_of_samples)

    if (plot_graph):
        # Create x and y arrays from the given data
        x_fit = [i for i in range(0,max_range+1)]
        y_fit = [expected_func(val+round(min_range)) for val in x_fit]

        # Create the matplotlib plot
        plt.figure(figsize=(8, 5)) 
        plt.plot(x, y, label='Experimental Data')
        plt.plot(x_fit, y_fit, color='red', label='Expected Data')
        plt.xlabel('func val')
        plt.ylabel('freq')
        plt.title(f'n={sample_size}, {human_format(number_of_samples)} samples, std error={round(std_error*100, 2)}%')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    # print(f'expected mean/sd: {round(test_collection_mean, 4)}/{round(test_collection_std_dev/(math.sqrt(sample_size)), 4)}')

    # print(f'experimental mean/sd: {round(sample_mean, 4)}/{round(sample_std_dev, 4)}')

    return std_error