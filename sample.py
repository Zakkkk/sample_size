import random
from utils import find_mean, progressBar
from numpy import std

def find_sample_mean(size, function):
    collection = []
    for i in range(size):
        collection.append(function(random.randint(0,99)))
    
    return find_mean(collection)

def find_sample_collection(sample_size, number_of_samples, function):
    samples_collection = []
    for i in progressBar(range(number_of_samples), prefix = 'Progress:', suffix = 'Complete', length = 50):
        samples_collection.append(find_sample_mean(sample_size, function)) 
        #perhaps divide sample mean bt number of samples

    return samples_collection, find_mean(samples_collection), std(samples_collection)
