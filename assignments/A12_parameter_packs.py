""" Assignment 12

Create a function with the `*args` parameter. The function should handle an
unbounded number of inputs without error. """

import statistics

def CR(*args):
    return statistics.mean(args)

levels = (16, 16, 16, 16, 14, 15, 11, 11, 5)

print(CR(*levels))