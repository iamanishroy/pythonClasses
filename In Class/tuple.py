'''
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")

thistuple = ("apple",)
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male", 100, "pqr")
tuple2 = (1, 5, 9, 3, 7)
tuple3 = (True, False, False)

print(tuple1[0])
print(tuple1[-1])
print(tuple1[2::2])
print(tuple1[1:4:2])  # start:end:step
print(tuple1[::-1])
print(tuple1[:3])
print(tuple1[3:6:1])
print(tuple1[2:])
'''

##############################
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))  # len

tuple4 = ("maths", "che", "phy", "bio")
tuple5 = (450, 700, 200)

print("Max value element : ", max(tuple4))  # max
print("Max value element : ", max(tuple5))

print("Min value element : ", min(tuple4))  # min
print("Min value element : ", min(tuple5))

aList = [123, "xyz", "zara", "abc"]
aTuple = tuple(aList)
print("Tuple elements : ", aTuple)

print((1, 2, 3) + (4, 5, 6))
print(("Hi!",) * 4)
for x in (1, 2, 3):
    print(x)

print(type(tuple4))
# tuple4[4] = "eng"
y = list(tuple4)
print(type(y))
print(y)
y.append("eng")
# y[1] = "phe"
print(y)
tuple4 = tuple(y)
print(tuple4)
