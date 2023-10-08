import random
from utils import find_mean
from numpy import std

def find_sample_mean(size, function):
    collection = []
    for i in range(size):
        collection.append(function(random.randint(0,100)+1))
    
    return find_mean(collection)

def find_sample_collection(sample_size, number_of_samples, function):
    samples_collection = []
    for i in range(number_of_samples):
        samples_collection.append(find_sample_mean(sample_size, function))

    return samples_collection, find_mean(samples_collection), std(samples_collection)