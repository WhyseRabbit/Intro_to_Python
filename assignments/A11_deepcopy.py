""" Assignment 11

Practice with deepcopy.

Try to devise an example where copy and deepcopy have different behavior.

Explain what happens in your example and why. """

wax = [12]
full = []
wane = []

phases = [wax, full, wane]

from copy import deepcopy

powers = deepcopy(phases)

wax.append(12)
full.append(23)

print(powers)