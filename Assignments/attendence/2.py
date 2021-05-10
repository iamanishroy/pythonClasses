# Accept age from user, check if the age is less than 18 display message
# you are minor and you are not eligible to work. If age is between 18 to 60
# display message eligible to work, fill your details and apply else display
# message too old to work, collect your pension using nested if else.

age = int(input('Enter the Age : '))

if age < 18:
    print('you are minor and you are not eligible to work')
else:
    if age <= 60:
        print('eligible to work, fill your details and apply')
    else:
        print('too old to work, collect your pension')
