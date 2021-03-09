# Write a python code to merge two sorted tuples.

def merge(list1, list2):
    merged = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(merge(list1, list2))
