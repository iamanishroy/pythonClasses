# Write a python program with a function for given a simple list of objects
# like string or integers as a parameter, checks whether there are duplicate
# elements in the list and return True of False accordingly. The input list
# should not be changed

items = [1, 'Anish', 5, 98, 'SICSR', 63, 'Anish']

itemsSet = list(set(items))

if(len(items) == len(itemsSet)):
    print(True)
else:
    print(False)

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
