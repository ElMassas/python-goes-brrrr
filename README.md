# python-goes-brrrr
Python is a very useful and easy language but it's not the fastest so I wanna see how fast I can make it with some relatively small changes.


# How to use

There's a Makefile on this repo, there will be commands to test every use case there. Just write: `make help` to see what's available

# Test scenarios

In order to test the speed and memory usage of the techonologies I am going to use, I will write some programs to test this.

**Test cases**:
 - Base Python with some simple loops
 - API
 - File manipulation
 - Matrices
 - String manipulation

I will also try and use different python versions were possible(some techonologies haven't gotten to the newer versions).

**Versions**:
 - 3.11
 - 3.12
 - 3.13

## Testing methodology

I am interested in testing the *speed*, *memory usage*, *stability*.
I will use different techniques to write some programs and will also use some different techonologies to run the programs.

### Techonologies

 - [CPython](https://cython.org/)
 - [Codon](https://github.com/exaloop/codon)
 - [Mojo](https://www.modular.com/max/mojo)
 - [Nuitka](https://github.com/Nuitka/Nuitka)
 - [Polars](https://pola.rs/) This will mostly be used instead of Pandas.
 - [Pypy](https://www.pypy.org/)

## Guidelines

To try and make the code generally fast to beging with, as well as readable, I will try to follow these guidelines:
 - Generally I will try to compile the code whenever possible.
 - Use list comprehensions and generators wherever is possible.
 - For some cases like I/O related operations and maths operations I will try to use Multiprocessing and threading(threading might show a larger improvemnet in Python 3.13 when not using the [GIL](https://realpython.com/python-gil/)).
 - Using While instead of For loops whenever it's reasonable, since for loops are known to be slow in python.
 - Use builtin functions whenever possible, because they are definitly faster then I can make them.
 - Only import what's required from a library
 - Use types.

---
# Resources

- [Speeding up python loops](https://medium.com/@nirmalya.ghosh/13-ways-to-speedup-python-loops-e3ee56cd6b73)
- [The art of speeding up python loops](https://towardsdatascience.com/the-art-of-speeding-up-python-loop-4970715717c)
