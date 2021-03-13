try:
    a = eval(input("Enter a Number : "))
    c = a / 1
except Exception as e:
    print(e)
else:
    a = a + 5
    print(a)