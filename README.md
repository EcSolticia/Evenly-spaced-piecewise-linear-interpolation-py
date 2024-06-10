# Evenly-spaced Piecewise Linear Interpolation

This repository features a python script for computing evenly spaced [piecewise linear interpolations](https://math.libretexts.org/Bookshelves/Applied_Mathematics/Numerical_Methods_(Chasnov)/05%3A_Interpolation/5.02%3A_Piecewise_Linear_Interpolation) of mathematical functions represented in the following form:

```python
def func(x):
  return x + x**2 - 1 #replace this with any real-valued mathematical function of x
```

## Discretization Parameters
The code features floats `start`, `end`, and `delta` as discretization parameters. 
* Mathematically, $`[start, end]`$ is the real interval in which the algorithm limits the input domain of the resulting function to.
* The float `delta` denotes the magnitude by which each input point for which the output is directly evaluated differ.
* If `start` and `end` are defined, `delta` must be chosen so that the maximal index is a natural number. If `start` or `end` is defined but not both, along with `delta`, then the undefined parameter must be defined so that the maximal index is a natural number. The program might not function as intended should the maximal index not be a natural.
* The execution of `max_index()` returns the maximal index.
* The variable `start` must be strictly smaller than `end` for any meaningful usage of the program.

## Indexing
Any real $`x`$ corresponds to an index through the following formula

$`x = start + index * delta`$

## Functions relating to indexing
* `index2value(i)`: Returns the value corresponding to the index $`i`$ through a direct application of the aforementioned formula.
* `value2index(x)`: Returns the index corresponding to the value x through a rearrangement of the indexing formula. The inverse function of `index2value(i)`.
* `index2func(i)`: Returns the function evaluated at the value corresponding to the $`i`$th index. A composition of `func(x)` to `index2value(i)`.
* No `value2func(x)` is needed given that `func(x)` is essentially such a function and serves such purpose.

## Central functions
* `compute_slopes()`: Computes the pertinent slopes for the sake of interpolation, storing values in the global list `slopes`.
* `slopepoint_func(x)`: Returns the evaluation of the interpolation at the value of $`x`$. Computes `slopes` if empty.
