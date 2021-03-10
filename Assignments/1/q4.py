# Write a python program to accept 10 numbers from the user and add even
# numbers in a list named “evennos” and odd numbers in a list named “oddnos”

nos = []
for i in range(10):
    nos.append(int(input("Enter the " + str(i + 1) + " number : ")))
evennos = []
oddnos = []

for no in nos:
    if(no % 2 == 0):
        evennos.append(no)
    else:
        oddnos.append(no)

print("Even Numbers : ", evennos)
print("Odd Numbers : ", oddnos)
