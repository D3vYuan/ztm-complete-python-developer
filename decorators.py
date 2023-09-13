# Higher Order Function HOC
def my_decorator(func):
    def wrap_func():
        print("*" * 10)
        func()
        print("*" * 10)
    return wrap_func

def my_decorator2(func):
    def wrap_func(*args, **kwargs):
        print("*" * 10)
        func(*args, **kwargs)
        print("*" * 10)
    return wrap_func

@my_decorator2
def hello_with_greetings(greeting, emoji = ":("):
    print(greeting, emoji)

@my_decorator
def hello():
    print("Helloooooo")

@my_decorator
def bye():
    print("See Ya Later!")

# hello()
# bye()

hello_with_greetings("hiiiiiiiiiii", ":)")
hello_with_greetings("bye")

# a = my_decorator(hello)
# a()

# my_decorator(hello)()