def fib_with_generator(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        print(f"#{i} (b4) - a: {a}, b: {b}")
        temp = a
        a = b
        b = temp + b
        print(f"#{i} (aft) - a: {a}, b: {b}")
        print("*" * 10)

def fib_with_list(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

for x in fib_with_generator(10000):
    print(x)

# print("*" * 10)
# print(fib_with_list(10000))