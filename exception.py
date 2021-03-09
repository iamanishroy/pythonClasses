a = 3
b = 1

'''
c = a / b
'''

try:
    c = a / b
except ZeroDivisionError:
    print('Calculation Error', 'zero value in denominator')


print('Hi there')
