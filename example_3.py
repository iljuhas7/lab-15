TextIO = open("file2.txt", "r")

content1 = TextIO.readline()
content2 = TextIO.readline()

print(content1)
print(content2)

TextIO.close()
