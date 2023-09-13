# list

my_list = [char for char in "Hello"]
my_list2 = [num for num in range(100)]
my_list3 = [num * 2 for num in range(100)]
my_list4 = [num * 2 for num in range(100) if num % 2 == 0]

for item in [my_list, my_list2, my_list3, my_list4]:
    print(item)
    print("-" * 50)

# set
my_set = {char for char in "Hello"}
my_set2 = {num for num in range(100)}
my_set3 = {num * 2 for num in range(100)}
my_set4 = {num * 2 for num in range(100) if num % 2 == 0}

for item in [my_set, my_set2, my_set3, my_set4]:
    print(item)
    print("-" * 50)

# dictionary
my_data = {
    "a": 1,
    "b": 2
}

my_dict = {key:value**2 for key, value in my_data.items()}
my_dict2 = {key:value**2 for key, value in my_data.items() if value % 2 == 0}
my_dict3 = {num:num*2 for num in [1, 2, 3]}

for item in [my_dict, my_dict2, my_dict3]:
    print(item)
    print("-" * 50)