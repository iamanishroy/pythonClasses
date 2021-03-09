# Write a python program to accept 10 numbers from the user and add even
# numbers in a list named “evennos” and odd numbers in a list named “oddnos”

nos = [1, 8, 2, 1, 5, 454, 41, 68, 31, 34, 6, 3, 13, ]
evennos = []
oddnos = []

for no in nos:
    if(no %2 == 0):
        evennos.append(no)
    else:
        oddnos.append(no)

print(evennos)
print(oddnos)
