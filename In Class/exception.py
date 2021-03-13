'''
a = 3
b = 0


c = a / b


try:
    c = a / b
except ZeroDivisionError:
    print('Calculation Error', 'zero value in denominator')


print('Hi there')


try:
    a = eval(input("Enter a number : "))
    print(3/a)
    raise NameError
except NameError:
    print("Please enter a number between 1 - 9.")
except ZeroDivisionError:
    print("Can not enter 0.")


try:
    a = eval(input("Enter a Number : "))
    c = a / 0
except Exception as e:
    print(e)
else:
    a = a + 5
    print(a)

'''
try:
    a = eval(input("Enter a number : "))
    print(3 / a)
except NameError:
    print("Please enter a number between 1 - 9")
except ZeroDivisionError:
    print("Can not enter 0.")
else:
    a = a + 5
    print(a)
finally:
    print("This block always execute.")

