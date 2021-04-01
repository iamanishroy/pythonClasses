# open and read file
my_file = open("E:/Python/In Class/test/test.txt", "r")
print(my_file.read())
my_file.close()

# create and write into a file
my_file2 = open("E:/Python/In Class/test/thursday.txt", "w+")
my_file2.write("Welcome to SICSR")
my_file2.seek(0)  # moves cursor to the 0th index
x = my_file2.read()
print(x)

# open and append file
my_file2 = open("E:/Python/In Class/test/thursday.txt", "a+")
my_file2.write('\nToday is Thursday')

# seek
my_file2.seek(10)
print(my_file2.tell())
print(my_file2.readline())  # reads only the current line
# my_file2.close()

# reading content line by line
my_file2.seek(0)
content = my_file2.readlines()
for x in content:
    print(x)

my_file2.close()
