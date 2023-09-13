def walrus_func():
    a = "hellloooooooooo"
    if ((n := len(a)) > 10):
        print(f"too long {n} elements")

    while ((n := len(a)) > 1):
        print(n)
        a = a[:-1]

    print(a)

if __name__ == "__main__":
    walrus_func()