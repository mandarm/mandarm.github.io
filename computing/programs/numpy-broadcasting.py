### Source: https://github.com/jakevdp/PythonDataScienceHandbook
## Broadcasting
import numpy as np

# Recall that for arrays of the same shape, binary operations are
# performed on an element-by-element basis.
# Also, binary ops with scalars ≡ pointwise op.
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
print(a + b)
print(a + 5)


## Operations on arrays of different (but compatible) shapes
# Simple example
M = np.ones((3, 3))
print(M + a)

# More complex example
a = np.arange(3)
b = np.arange(3).reshape(3,1)
print(a+b)


## More examples
# Example 1
M = np.ones((2, 3))
a = np.arange(3)
print(M + a)
# Explanation
# M.shape is (2, 3), a.shape is (3,)
# => a.shape becomes (1, 3)     (by rule 1)
# => a.shape becomes (2, 3) by copying/broadcasting     (by rule 2)

# Example 2
a = np.arange(3).reshape((3, 1))
b = np.arange(3)
print(a+b)
# Explanation
# - a.shape is (3, 1)
# - b.shape is (3,)
#
# Rule 1 says we must pad the shape of b with ones:
#
# - a.shape remains (3, 1)
# - b.shape becomes (1, 3)
#
# And rule 2 tells us that we must upgrade each of these 1s to match
# the corresponding size of the other array:
#
# - a.shape becomes (3, 3)
# - b.shape becomes (3, 3)
#
# Because the results match, these shapes are compatible for pointwise +.

# Example 3
M = np.ones((3, 2))
a = np.arange(3)
print(M+a)   # DOES NOT WORK
# Explanation
# - M.shape is (3, 2)
# - a.shape is (3,)
#
# Again, rule 1 tells us that we must pad the shape of a with ones:
#
# - M.shape remains (3, 2)
# - a.shape becomes (1, 3)
#
# By rule 2, the first dimension of a is then stretched to match that of M:
#
# - M.shape remains (3, 2)
# - a.shape becomes (3, 3)
#
# Now we hit rule 3—the final shapes do not match, so these two arrays
# are incompatible, as we can observe by attempting this operation:


## Application: centering an Array
rng = np.random.default_rng(seed=1701)
X = rng.random((10, 3))    # Initial data
Xmean = X.mean(0)          # Mean of each column
X_centered = X - Xmean     # Needs broadcasting
print(X_centered.mean(0))  # Sanity check
