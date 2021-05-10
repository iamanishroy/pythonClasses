# Write a Python program to count the frequency of words in a file.

my_file = open("E:/Python/Assignments/attendence/sampleFile.txt", "r")
string = my_file.read()
my_file.close()
freqDict = {}


for word in string.split():
    if word in freqDict.keys():
        freqDict[word] = freqDict[word] + 1
    else:
        freqDict[word] = 1

for word in freqDict:
    print(word + '->', freqDict[word])
