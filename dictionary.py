'''
mydict = {
    "brand": "Ford",
    "model": "Figo",
    "year": 2000,
    "color": ["red", "white"]
}
print(mydict)
print(mydict["brand"])


mydict1 = {
    "brand": "Ford",
    "model": "Figo",
    "year": 2000,
    "year": 2001
}
print(mydict1)

# finding length
print(len(mydict))
print(len(mydict1))

# update
mydict1["brand"] = "Maruti"
print(mydict1)

# add
mydict1["price"] = "8L"
print(mydict1)

# delete
del mydict1["year"]  # 1st way
print(mydict1)

Dict = {
    1: "JavaTpoint",
    2: "Peter",
    3: "Thomas"
}
pop_ele = Dict.pop(3)  # 2nd way
print(Dict)
Dict.popitem()  # delete from last
print(Dict)
Dict.clear()  # clear the dictionary
print(Dict)
'''

# print all keys
Employee = {
    "Name": "Jhon",
    "Age": 29,
    "salary": 25000,
    "Company": "GOOGLE"
}

for x in Employee:
    print(x)
print("\n")

for x in Employee:
    print(Employee[x])
print("\n")

for x in Employee.values():
    print(x)
print("\n")

for x in Employee.items():
    print(x)

city = input("What part of Mahaeashtra did you visit? ")
answer = f"Great, {city} is an interesting city!"
print(answer)
