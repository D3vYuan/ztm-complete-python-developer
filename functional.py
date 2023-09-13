# map, filter, zip, reduce

from functools import reduce 

my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = [5, 4, 3]

def multiply_by_2(item):
    return item * 2

def only_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(list(map(multiply_by_2, [1, 2, 3])))
print(list(filter(only_odd, [1, 2, 3, 4])))
print(list(zip(my_list, your_list, their_list)))
print(reduce(accumulator, my_list, 0))