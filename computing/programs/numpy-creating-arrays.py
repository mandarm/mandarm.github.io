### Source: https://github.com/jakevdp/PythonDataScienceHandbook
## Creating Arrays from Scratch

# Create an uninitialized array of three integers; the values will be
# whatever happens to already exist at that memory location
A = np.empty(3)

# Create a 3x5 floating-point array filled with 1s
A = np.ones((3, 5), dtype=float)

# Create a length-10 integer array filled with 0s
A = np.zeros(10, dtype=int)

# Create a 3x5 array filled with 3.14
A = np.full((3, 5), 3.14)

# Create a 3x3 identity matrix
A = np.identity(3)


# Create an array filled with a linear sequence starting at 0, ending
# at 20, stepping by 2 (this is similar to the built-in range
# function)
A = np.arange(0, 20, 2)

# Create an array of five values evenly spaced between 0 and 1
A = np.linspace(0, 1, 5)


# Create a 3x3 array of uniformly distributed pseudorandom values
# between 0 and 1
A = np.random.random((3, 3))

# Create a 3x3 array of normally distributed pseudorandom values with
# mean 0 and standard deviation 1
A = np.random.normal(0, 1, (3, 3))

# Create a 3x3 array of pseudorandom integers in the interval [0, 10)
A = np.random.randint(0, 10, (3, 3))
