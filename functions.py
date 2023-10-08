import math

# All functions are between 1 and 100 inclusive, whole numbers
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

def upside_normal(x):
    return 50 - 1000/(math.sqrt(2*math.pi) * 12) * math.exp(-1/2 * ((x-50)/12)**2)
