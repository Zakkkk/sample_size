from functions import *
from function_information import *
import random

def create_sample(size, function):
    collection = []
    for i in range(size):
        collection.append(function(random.randint(1,100)))
    
    return find_sample(collection)

sample_size = int(input('Sample size: '))
samples_mean, samples_std_dev = 0, 0

for i in range(1000000):
    sample_collection = []
    sample_collection.append(create_sample(sample_size, linear)[0]) # choose function type here
    samples_mean, samples_std_dev = find_sample(sample_collection)

true_mean, true_std_dev = find_true(linear)
print(f"The mean is expected to be {true_mean} and the std dev is expected to be {true_std_dev/math.sqrt(sample_size)}\n")

print(f"The actual mean is {samples_mean} and the actual std dev is {samples_std_dev}\n")
