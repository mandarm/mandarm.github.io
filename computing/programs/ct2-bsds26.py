# "Boilerplate"
import math

import numpy as np
import pandas as pd

rng = np.random.default_rng()

#---------------------------------------------------------------------------#

# 1(a)
# Let \texttt{A} be a NumPy ndarray. Given the attributes
# \texttt{A.itemsize} and \texttt{A.shape}, write Python
# \textbf{statements} to compute the attributes \texttt{A.ndim},
# \texttt{A.size} and \texttt{A.nbytes} in terms of the given
# attributes and/or attributes calculated earlier.

A = np.array([ i for i in range(71,95) ]).reshape(4, 6)

print(A.ndim == len(A.shape))

print(A.size == math.prod(A.shape))
# OR
print(A.size == np.prod(A.shape))
# OR
s = 1
for d in A.shape: s *= d
print(A.size == s)

print(A.nbytes == A.size * A.itemsize) # or any equivalent


# 1(b)
A = np.linspace(5, 19, 8).reshape(2, 4)
# [[ 5.,  7.,  9., 11.],
#  [13., 15., 17., 19.]]

B = np.linspace(20, 41, 8).reshape(4, 2)
# [[20., 23.],
#   26., 29.],
#   32., 35.],
#   38., 41.]]

C = np.concat([A[0:2,1:3], B[1:3,0:2]], axis=1)
# A[0:2,1:3] = [[ 7.,  9.],
#               [15., 17.]]
# B[1:3,0:2] = [[26., 29.],
#                [32., 35.]]
# C = [[ 7.,  9., 26., 29.],
#      [15., 17., 32., 35.]]

D = A.sum(axis=0)
# [18., 22., 26., 30.]

E = C + D
# [[25., 31., 52., 59.],
#  [33., 39., 58., 65.]]

#---------------------------------------------------------------------------#

A = np.array([ i for i in range(71,95) ]).reshape(4, 6)
pdA = pd.DataFrame(A, index=["Gupi", "Bagha", "Haru", "Bhombol"], 
                   columns=list("123456"))

# 2(a)
# The teacher for \textbf{course 1 forgot to include marks for the
# homework component of the course in the total, and submits these
# marks separately. These marks are stored in a Python list hw (with 4
# elements for the above example). Write code to update pdA with the
# correct scores for course 1.
pdA.loc[:,"1"] += np.array(hw) # OR simply hw (np.array is not needed)


# 2(b)
# Write a Python statement to calculate the mean score for each course.
np.mean(A, axis=0)
# OR
pdA.mean(axis=0)


# 2(c)
# Write Python statements to calculate each student's aggregate and
# overall percentage.
agg = np.sum(A, axis=1) # OR
agg = pdA.sum(axis=1)

percentage = agg/6


# 2(d)
# Write code to construct a list containing the names of all students
# in alphabetically sorted order.
l = sorted(pdA.index)


# 2(e)
# Use list comprehension to generate a list of roll numbers from the
# above list. Roll numbers have to be of the form BSDS26XX, where XX
# is a 2 digit number (assume that the number of students is less than
# 100). These should be assigned to the students in alphabetic order
# starting with BSDS2601, BSDS2602, ...
rolls = [ f"BSDS26{r+1:02d}" for r in range(pdA.shape[0]) ] # or equivalent 


# 2(f)
# Construct another DataFrame pdB with a single column named "RollNo"
# and an index given by the list constructed in part (d). The entries
# in the single column should be the roll numbers generated in part
# (e).
pdB = pd.DataFrame(rolls, index=l, columns=["RollNo"])


# 2(g)
# Show how you would correctly combine the information in DataFrames
# pdA and pdB.
pd.concat([pdA,pdB], axis=1) # OR
pdA.join(pdB)
