# Write a python program to accept values for two points in a plane i.e (x1,y1) and (x2,y2).
# Write an exception if value is string or other than number is entered by user otherwise
# display  the distance between two points using formula- dist = math.sqrt((x2-x1)*2 + (y2-y1)*2)

import math
x1 = int(input("Enter the value of x1 : "))
x2 = int(input("Enter the value of x2 : "))
y1 = int(input("Enter the value of y1 : "))
y2 = int(input("Enter the value of y2 : "))

# TODO: handel exception
try:
    print(math.sqrt((x2-x1)*2 + (y2-y1)*2))
except TypeError:
    print("Entered value must be a number")
