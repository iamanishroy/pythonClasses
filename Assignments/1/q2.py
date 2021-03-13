# Write a python program with a function for given a simple list of objects
# like string or integers as a parameter, checks whether there are duplicate
# elements in the list and return True of False accordingly. The input list
# should not be changed

def checkDuplicates(items):
    itemsSet = list(set(items))
    return len(items) == len(itemsSet)


items = []
length = int(input("Enter the number of items to be entered : "))
for i in range(length):
    items.append(input("Enter the " + str(i + 1) + " item : "))
print(checkDuplicates(items))

# itemsLength = len(items)
# counter = 1
# found = False
# for item in items:
#     i = counter
#     for i in range(counter, itemsLength):
#         if item == items[i]:
#             found = True
#             break
#     counter = counter + 1
# print(found)
