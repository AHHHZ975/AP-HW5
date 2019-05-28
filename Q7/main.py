import numpy

input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 12]
print(" ".join(str(element) for element in numpy.unique(sorted([value for (index, value) in enumerate(input) if (value % 6 is 0) and ((index+1) % 6 is 0)]))))