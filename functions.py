import math

# All functions are between 0 and 100, whole numbers
def exponential(x):
    return math.exp(x/25)

def linear(x):
    return x

def sinusoidal(x):
    return 50 + 20 * math.sin(math.pi * x / 25)

def absolute(x):
    return abs(x-75) + abs(x-25) + (abs(x-60)+abs(x-40))/2

def ellipse(x):
    return math.sqrt(x*(100-x))