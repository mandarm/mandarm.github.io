# "Boilerplate"
import math

import numpy as np

rng = np.random.default_rng()

#---------------------------------------------------------------------------#

# 1(a)
# Let $A$ be a matrix that is stored as a list of lists (all of which
# are of the same length). Write code to create $A^T$ the transpose of
# $A$ ($A^T$ should also be stored as a list of lists). For full
# credit, your code should be a one-line, list comprehension
# expression.
A = rng.integers(20, size=(3,4))
A_transpose = [ [ row[i] for row in A ] for i in range(len(A[0])) ]
print(f'{A}\n{A_transpose}')

A = rng.integers(40, size=(5,4))
A_transpose = [ [ row[i] for row in A ] for i in range(len(A[0])) ]
print(f'{A}\n{A_transpose}')

# GRADING GUIDELINES
# Using range(len(A)) instead of range(len(A[0])) (works only for
# square matrices => deduct 0.5


# 1(b)
# Suppose that the entries of $A$ are all strings. Write code to
# create a string that is obtained by concatenating all the entries of
# $A$ in row-major order. For full credit, your code should be a
# one-line, list comprehension expression.
A = [ [ "a", "b", "c" ], [ 'x', 'y', 'z' ], [ 'p', 'q', 'r' ],
      [ 'haru', 'gupi', 'bagha' ] ]
s1 = ''.join([A[i][j] for i in range(len(A)) for j in range(len(A[0]))])
s2 = ''.join(element for row in A for element in row)
print(f'{s1}\n{s2}\n{s1 == s2}')

# GRADING GUIDELINES 
# Returning a list of strings (one per row) instead of a single
# concatenated string => deduct 1


# 1(c)
# Confusing row-major traversal and column-major traversal, or doing
# row-major (or column-major) traversal for both parts => no penalty

#---------------------------------------------------------------------------#

# 2
# Write a Python function \texttt{merge\_dict(d1, d2)} that takes two
# dictionaries \texttt{d1}, \texttt{d2} as arguments, and returns a
# dictionary that contains all keys in \texttt{d1} and \texttt{d2}. If
# \texttt{d1} and \texttt{d2}, share any keys, the value for such keys
# in the result should be the sum of the corresponding values from
# \texttt{d1} and \texttt{d2} (you may assume these are both
# integers). For example, if \texttt{dict1 = \{"a": 10, "b": 20, "c":
# 30\}} and \texttt{dict2 = \{"b": 5, "c": 15, "d": 25\}}, your
# function should return \texttt{\{"a": 10, "b": 25, "c": 45, "d":
# 25\}}. The order of the keys in the result is not important.
def merge_dict(d1, d2):
    merged = d1 | d2
    for k in merged:
        if k in d1 and k in d2: 
            merged[k] += d1[k]
    return merged
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 25}
print(merge_dict(dict1, dict2))

#---------------------------------------------------------------------------#

# 3
# Recall that if $f(x)$ is continuous over $[a,b]$ \[ \int_a^b f(x) dx
#  ~=~ \lim_{n \ra \infty} \sum_{i=0}^{n-1} f\big(a + \frac{i}{n}
#  (b-a)\big) \times \frac{b-a}{n}. \] 
# Write a Python function \texttt{integrate(f, a, b)} that uses the
# above idea to compute $\displaystyle \int_a^b f(x) dx$. Use a fixed
# value of $n=10^3$ in your code.
n = 1_000_000
def integrate1(f, a, b):
    h = (b-a) / n
    return sum((f(a + i*h) for i in range(n)))*h

print(integrate1(lambda x: x*x, 1.5, 2.5))
print(integrate1(math.exp, 1.0, 3.5))
print(integrate1(lambda x: (math.exp(-(x*x)/2))/((2*math.pi)**0.5), -1, 1))
print(integrate1(lambda x: (math.exp(-(x*x)/2))/((2*math.pi)**0.5), -2, 2))
print(integrate1(lambda x: (math.exp(-(x*x)/2))/((2*math.pi)**0.5), -3, 3))

# Also need to think about how to do this in numpy. Hope to add
# supplementary material to the slides.

#---------------------------------------------------------------------------#

# 4
# A number is said to be a \emph{Disarium Number} if the sum of its
# digits raised to their respective positions is the number itself.
# The position of the leftmost significant digit is defined as 1;
# subsequent digits to the right are assigned positions 2, 3, \dots.
# For example, 135 and 518 are Disarium Numbers, since $1^1 + 3^2 +
# 5^3 = 1 + 9 + 125 = 135$, and $5^1 + 1^2 + 8^3 = 518$. Single digit
# numbers are all Disarium Numbers, but 75 ($7^1 + 5^2 = 7 + 25 = 32$)
# and 544 are not.
# Write a Python function \texttt{is\_disarium(n)} that returns
# \texttt{True} if \texttt{n} is a Disarium Number, and \texttt{False}
# otherwise.
def is_disarium1(n):
    s = str(n)
    d = sum( int(c)**(i+1) for i, c in enumerate(s) )
    # OR
    # d = sum( (ord(c) - ord('0'))**(i+1) for i, c in enumerate(s) )
    return d == n

def is_disarium2(n):
    saved_n = n
    num_digits = int(math.log10(n)) + 1
    # print(num_digits)
    disarium_sum = 0
    while n:
        i = n % 10
        disarium_sum += i**num_digits
        # print(disarium_sum)
        n //= 10
        num_digits -= 1
    return disarium_sum == saved_n

print(f"""135: {is_disarium1(135)} {is_disarium2(135)}
518: {is_disarium1(518)} {is_disarium2(518)}
1: {is_disarium1(1)} {is_disarium2(1)}
5: {is_disarium1(5)} {is_disarium2(5)}
75: {is_disarium1(75)} {is_disarium2(75)}
544: {is_disarium1(544)} {is_disarium2(544)}""")

# GRADING GUIDELINES
# Using str(n).split(' , ') to convert an integer to the list of its
# digits => deduct 1

# Initialising variable for sum of digits outside the function, and
# attempting to update within the function without global => deduct 0.5

# Forgetting to convert to str(n) and/or int(c) => deduct 1 if one
# conversion is missing; 1.5 if both are missing.
