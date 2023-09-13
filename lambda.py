from functools import reduce

my_list = [1, 2, 3]

print(list(map(lambda x : x * 2, my_list )))
print(list(filter(lambda x : x % 2 == 0, my_list )))
print(reduce(lambda acc, x : acc + x, my_list ))