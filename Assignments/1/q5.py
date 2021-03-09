# Write a python program to accept 10 numbers from the user and store
# it in the list. Add only multiples of 4 from the stored list and
# display its sum.

nos = [1, 8, 2,]
sum = 0
for no in nos:
    if(no % 4 == 0):
        sum = sum + no
print(sum)
