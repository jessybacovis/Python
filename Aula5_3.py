# Python program to demonstrate
# the use of index arrays.
import numpy as np

# Create a sequence of integers from
# 10 to 1 with a step of -2
a = np.arange(10, 1, -2)
print("\n A sequential array with a negative step: \n",a)

# Indexes are specified inside the np.array method.
newarr = a[np.array([3, 1, 2 ])]
print("\n Elements at these indices are:\n",newarr)
