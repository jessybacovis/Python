import numpy as np

macros = np.array([
[0.8, 2.9, 3.9],
[52.4, 23.6, 36.5],
[55.2, 31.7, 23.9],
[14.4, 11, 4.9]
])

# Create a new array filled with zeros,
# of the same shape as macros.
result = np.zeros_like(macros)

cal_per_macro = np.array([3, 3, 8])

# Now multiply each row of macros by
# cal_per_macro. In Numpy, `*` is
# element-wise multiplication between two arrays.
for i in range(macros.shape[0]):
result[i, :] = macros[i, :] * cal_per_macro
result