### Source: https://github.com/jakevdp/PythonDataScienceHandbook
## Concatenation of Arrays
import numpy as np

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = np.array([99, 99, 99])
w = np.array([[99], [99]])


# np.concatenate()
# 1-D arrays
print(np.concatenate([x, y]))      # [1 2 3 3 2 1]
print(np.concatenate([x, y, z]))   # [1 2 3 3 2 1 99 99 99]

# 2-D arrays
grid = np.array([[1, 2, 3], [4, 5, 6]])

print(np.concatenate([grid, grid])) # default axis = 0
print(np.concatenate([grid, grid], axis=1))
print(np.concatenate([grid, grid], axis=None))


# np.vstack,`np.hstack
print(np.vstack([x, y]))      # Note difference with concatenate above
print(np.vstack([x, grid]))
print(np.hstack([x, y]))      # Same as concatenate above
print(np.hstack([grid, w]))


## Splitting of Arrays
x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)           # [1 2 3] [99 99] [3 2 1]

x = np.arange(8.0)
np.split(x, [3, 5, 6, 10])  # 10 > size => last split is empty

# 3-D arrays
x = np.arange(8.0).reshape(2, 2, 2)
np.hsplit(x, 2)
# -> [array([[[0.,  1.]], [[4.,  5.]]]), array([[[2.,  3.]], [[6.,  7.]]])]
np.vsplit(x, 2)
# -> [array([[[0., 1.], [2., 3.]]]), array([[[4., 5.], [6., 7.]]])]

grid = np.arange(16).reshape((4, 4))
upper, lower = np.vsplit(grid, [2])
print(upper)   # [[0 1 2 3] [4 5 6 7]]
print(lower)   # [[8 9 10 11] [12 13 14 15]]

left, right = np.hsplit(grid, [2])
print(left)    # [[0 1] [4 5] [8 9] [12 13]]
print(right)   # [[2 3] [6 7] [10 11] [14 15]]
