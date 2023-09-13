# generator generates number 1 by 1, nothing is stored in memory; 
# whereas list store the values in memory

def generator_function(num):
    for i in range(num):
        yield i * 2

# for item in generator_function(10):
#     print(item)

g = generator_function(10)
next(g)
next(g)
print(next(g))