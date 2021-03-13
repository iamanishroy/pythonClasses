# Write a python code to merge two sorted tuples.

tuple1 = (1, 8, 12, 44, 95,)
tuple2 = (5, 78, 96, 155,)

list3 = []
i, j = 0, 0

while len(tuple1) > i and len(tuple2) > j:
    if tuple1[i] < tuple2[j]:
        list3.append(tuple1[i])
        i = i + 1
    else:
        list3.append(tuple2[j])
        j = j + 1

if len(tuple1) != i:
    while i < len(tuple1):
        list3.append(tuple1[i])
        i = i + 1

elif len(tuple2) != j:
    while j < len(tuple2):
        list3.append(tuple2[j])
        j = j + 1

print("Sorted and Merged Tuple : ", tuple(list3))
