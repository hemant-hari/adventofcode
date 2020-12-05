import numpy as np

array = []
f = open("input.txt")
for line in f:
    array.append(int(line))

array.sort()
for i, n in enumerate(array):
    for m in array:
        for o in array:
            if (m + n + o) == 2020:
                print(m*n*o)