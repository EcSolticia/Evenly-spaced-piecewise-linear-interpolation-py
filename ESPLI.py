
from math import floor

# the mathematical function
def func(x):
    return x**2

# discretization parameters
start = 0
end = 5.0 #ensure that this matches with delta
delta = 0.1

def max_index():
    output_raw = (end - start)/delta
    return int(output_raw)

def index2value(i):
    return start + i*delta
    
# ensure that input = index2value(i) for some i
def value2index(x):
    return (x - start)/delta
    
def index2func(i):
    input = index2value(i)
    return func(input)
    
# ---- #

slopes = []
def compute_slopes():
    global slopes
    slopes = []
    
    for i in range(max_index() - 1):
        this_slope = (index2func(i + 1) - index2func(i))/delta
        slopes.append(this_slope)     


def slopepoint_func(x):
    global slopes
    if len(slopes) == 0:
        compute_slopes()    
        
    if x == end:
        return func(end)
    
    x_i = index2value(floor(value2index(x)))
    
    i = int(value2index(x_i))
    output = slopes[i]*(x - x_i) + func(x_i)
    return output
