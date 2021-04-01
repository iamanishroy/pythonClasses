# Write a python program to accept number of words from user then accept
# and print the words together on one line. Display exception if for
# number integer value is not provided from user at start.
# import this
try:
    wordCount = int(input('Enter the count of words : '))
    words = []
    for i in range(wordCount):
        words.append(input('Enter the ' + str(i+1) + ' word : '))
    line = ''
    for word in words:
        line = line + word + ' '
    print(line)
except ValueError:
    print("Word count must be an Integer Value")
