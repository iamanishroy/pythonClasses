# groceries = []
# groceries = ["milk", "bread", "eggs"]
# print(groceries)
# print(groceries[0])
# print(groceries[1])
# print(groceries[2])
# print(groceries[0:2])
# groceries[0] = 'cheese'
# print(groceries)

# mylist = [1, '2', 3.0, False]
# print(mylist)

# mylist1 = [5,
#            2,
#            1,
#            [0.2, 0.3, "a", [11, 22, 33]], ["aa", "bb", 11],
#            3, 7]
# print(mylist1)
# print(mylist1[0])
# print(mylist1[1])
# print(mylist1[3])
# print(mylist1[4])
# print(mylist1[4][1])
# print(mylist1[3][2])
# print(mylist1[3][3][1])
# print(mylist1[4][2])

# sliced_List = mylist1[2:4]  # returns 2 to (4-1) elements
# print(sliced_List)

# len_mylist1 = len(mylist1)  # return length of the list
# print(len_mylist1)
# print(mylist1[4-len_mylist1][1])
# print(mylist1)

# mylist1.remove(2)  # remove given value removes '2' not index 2
# print(mylist1)

# mylist1.pop()  # removes and returns last element
# print(mylist1)

# mylist1.insert(1, 22)  # update 1 index with 22 and shifts rest elements
# print(mylist1)

mylist2 = [5, 3, 7, 2, 8, 9, 1]
mylist2.sort()
print(mylist2)

mylist2.sort(reverse=True)
print(mylist2)

mylist2.append(4)
print(mylist2)
print("maximum:", max(mylist2))
print("minimum:", min(mylist2))
print("sum:", sum(mylist2))

l1 = [70, 20]
l2 = [30, 10]
l1.extend(l2)
print(l1)

print(sorted(l1)) # sorted temporarily
print(l1)
l1.sort() # sorted permanently
print(l1)
