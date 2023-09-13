files = {
    "A": ["B", "C", "D.txt"],
    "B": ["E", "F", "G.txt"],
    "C": ["H.txt"],
    "E": ["I"],
    "I": ["J.txt", "K", "L"],
    "K": ["M.txt"],
    "L": ["N.txt"]
}

file_sizes = {
    "D.txt": 30,
    "G.txt": 20,
    "H.txt": 10,
    "J.txt": 40,
    "M.txt": 70,
    "N.txt": 5,
}

import os

class MinHeap():
    def __init__(self, size):
        self.heap = []
        self.size = size

    def swap(self, item):
        current_item_size = item[-1]
        for idx, heap_item in enumerate(self.heap):
            current_heap_item_size = heap_item[-1]
            if(current_item_size > current_heap_item_size):
                print(f"{item} insert @{idx}")
                self.heap.insert(idx, item)
                return
        self.heap.insert(len(self.heap), item)

    def insert(self, item):
        smallest_item_size = -999999
        if (len(self.heap) > 0):
            smallest_item = self.heap[-1]
            smallest_item_size = smallest_item[-1]

        current_item_size = item[-1]

        if (current_item_size > smallest_item_size and len(self.heap) >= self.size):
            # print(f"{item} [{current_item_size}] > {smallest_item} [{smallest_item_size}]")
            self.swap(item)
            print(self.heap)
        elif (len(self.heap) < self.size):
            print(f"{item} appending to heap")
            self.swap(item)
            print(self.heap)
        else:
            print(f"{item} [{current_item_size}] < {smallest_item} [{smallest_item_size}]")

        while(len(self.heap) > self.size):
            print(f"removing last item as heap size {len(self.heap)} is bigger than {self.size}")
            del self.heap[-1]

    def print(self):
        for idx, item in enumerate(self.heap):
            item_size = item[-1]
            item_name = item[0]
            print(f"#{idx + 1} - {item_size}    {item_name}")

def performance(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return result
    return wrapper

def get_files(dir):
    if dir in files:
        return files[dir]
    return []

def get_file_size(path):
    if path in file_sizes:
        return file_sizes[path]
    return None

def is_file(path):
    # return os.path.isfile(path)
    filename = os.path.basename(path)
    if "." in filename:
        return True
    else:
        return False

@performance
def get_list_of_files_recursive(dir):
    list_of_files = []
    for file in get_files(dir):
        if is_file(file):
            print(f"Processing: {file}")
            list_of_files.append(file)
        else:
            list_of_files.extend(get_list_of_files_recursive(file))
    return list_of_files

@performance
def get_list_of_files_stack(dir):
    stack = []
    pass

@performance
def get_largest_by_sorting(list_of_files, topk = 5):
    if len(list_of_files) <= 0:
        return
    
    list_of_file_sizes = [(x,get_file_size(x)) for x in list_of_files]
    print(list_of_file_sizes)

    sorted_list = sorted(list_of_file_sizes, key=lambda x: x[1], reverse=True)
    print(sorted_list)

    for item in range(topk):
        item_pair = sorted_list[item]
        print(f"{item_pair[1]}  {item_pair[0]}")

@performance    
def get_largest_by_heap(list_of_files, topk=5):
    if len(list_of_files) <= 0:
        return
    
    heap = MinHeap(topk)
    for file in list_of_files:
        file_size = get_file_size(file)
        heap.insert((file, file_size))

    heap.print()

if __name__ == "__main__":
    # list_of_files = get_list_of_files_recursive("A")
    # print(list_of_files)

    list_of_files = get_list_of_files_stack("A")
    print(list_of_files)

    # get_largest_by_sorting(list_of_files, 5)
    # get_largest_by_heap(list_of_files, 5)
    