
def arguments_func(*args):
    """
    INFO: Accept any length of arguments
    """
    print(args)
    print(f"Total (args): {sum(args)}")

def keyword_arguments_func(**kwargs):
    """
    INFO: Accept keyword arguments
    """
    print(kwargs)
    for item in kwargs.values():
        print(item)

    for item in kwargs:
        print(f"{item}: {kwargs[item]}")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

    total = sum([ x for x in kwargs.values() ])
    print(f"Total (kwargs): {total}")

if __name__ == "__main__":
    arguments_func(1, 2, 3, 4, 5)
    keyword_arguments_func(num1 = 5, num2 = 10)
