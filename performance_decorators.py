from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"took {t2 - t1} s")
        return result
    return wrapper

@performance
def long_time_generator():
    for i in range(100000000):
        i * 5

@performance
def long_time_list():
    for i in list(range(100000000)):
        i * 5

long_time_generator()
long_time_list()
