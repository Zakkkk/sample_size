import math
import numpy as np

# All functions are between 0 and 99 inclusive, whole numbers
def exponential(x):
    return math.exp(x/25)

def linear(x):
    return x

def sinusoidal(x):
    return 50 + 20 * math.sin(math.pi * x / 25)

def absolute(x):
    return abs(x-75) + abs(x-25) + (abs(x-60)+abs(x-40))/2

def ellipse(x):
    return math.sqrt(abs(x*(100-x)))

def normal(x, m=50, s=12):
    return 1 / (s * math.sqrt(2 * math.pi)) * np.exp(-1 / 2 * ((x - m) / s)**2)

def upside_normal(x):
    return 50 - 1000*normal(x, 50, 12)

def quadratic(x):
    return (x-50)**2 / 25
