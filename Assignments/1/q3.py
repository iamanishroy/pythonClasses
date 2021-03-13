# Write a python program (with user input) to create tuple of elements with
# different datatype. Then display tuple with element having similar datatype.
# (In short classify and display tuple with similar datatype element)

mixed = (1, 'aa1', 151654, 'Python', True, '99', 'A', False, True)
dataTypes = []
classified = []

for data in mixed:
    tyC = 0
    for dataType in dataTypes:
        if(type(data) == dataType):
            classified[tyC].append(data)
            break
        tyC = tyC + 1
    else:
        dataTypes.append(type(data))
        classified.append([data, ])

print("Classified Tuples :- ")
for types in classified:
    print(tuple(types))
