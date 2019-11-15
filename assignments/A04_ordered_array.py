""" Assignment 4

1. Turn the jumbled_nums tuple into a list.
2. Add the value 5 to the list.
3. Remove one of the values of 4 from the list.
4. Then sort the list.
5. Insert the value 1 at the beginning of the list.
6. Turn the list back into a tuple.
7. Finally print the list. """

jumbled_nums = (8, 4, 2, 9, 7, 3, 6, 4)


# Answer
list_nums = list(jumbled_nums)
list_nums.append(5)
list_nums.remove(4)
list_nums.sort()
list_nums.insert(0, 1)
tuple_nums = tuple(list_nums)
print(tuple_nums)
