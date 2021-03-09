'''
1.WAP to add two nos.
2 .WAP to print the given no. is even or odd
3. WAP to print reverse of a given no.
4. WAP to print armstrong of a given no. e.g 153=1+125+27=153
'''

# n1 = int(input("Enter the first number : "))
# n2 = int(input("Enter the second number : "))
# sum = n1 + n2
# print(sum)

# number = int(input("Enter the number : "))
# if number % 2 == 0:
#     print("The number is Even")
# else:
#     print("The number is Odd")

# num = int(input("Enter the number : "))
# rev = 0
# while(num > 0):
#     rev = rev * 10
#     rev = rev + (num % 10)
#     num = num // 10
# print(rev)


def checkArmstrong(num):
    temp = num
    numSum = 0
    while(temp > 0):
        cube = (temp % 10) ** 3
        numSum = numSum + cube
        temp = temp // 10
    return num == numSum


print(checkArmstrong(int(input("Enter the number : "))))
