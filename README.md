# knockoffspy

An interface to [Knockoffs.jl](https://github.com/biona001/Knockoffs.jl) from the Python programming language. `knockoffspy` provides unique high performance methods for sampling various model-X knockoffs and ships with built-in routines for variable selection. Much of the functionality are unique and allow for orders of magnitude speedup over conventional methods. 'knockoffspy' attaches a Python interface onto the package, allowing seamless use of this tooling by Python users. 

## Installation

To install `knockoffspy`, use pip:
```
pip install knockoffspy
```
Then in the python interpreter,
```python
>>> import knockoffspy
>>> knockoffspy.install()
```