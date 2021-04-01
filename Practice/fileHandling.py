'''
read file, display content, create a new file and add content of old file to new file and display the content
'''

file = open("E:/Python/Practice/sample/text.txt", "r")
print(file.read())
# file.close()

new_file = open("E:/Python/Practice/sample/new_text.txt", "w+")
new_file.write("file")
print(new_file.read())
