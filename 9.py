import math

def binary_search(collection, item):
    left = 0
    right = len(collection) - 1

    while True:
        if left > right:
            return -1
        middle = math.floor((left + right) / 2)
        if collection[middle] < item:
            left = middle + 1
        elif collection[middle] > item:
            right = middle - 1
        elif collection[middle] == item:
            return middle



sequence = sorted([1, 6, 8, 3, 2, 7, 11, 42])

print(sequence)

first_index = binary_search(sequence, 6)
second_index = binary_search(sequence, 9)
third_index = binary_search(sequence, 11)

print(6, "is at index", first_index)
print(9, "is at index", second_index)
print(11, "is at index", third_index)