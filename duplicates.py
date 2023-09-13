some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

def identify_duplicates():
    duplicates = []
    for value in some_list:
        if some_list.count(value) > 1:
            if value not in duplicates:
                duplicates.append(value)

    print(duplicates)

if __name__ == "__main__":
    # print("Hello World")
    print(some_list)
    identify_duplicates()

