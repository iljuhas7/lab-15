import os

with open("file2.txt", "w") as TextIO:
    TextIO.write("File2.txt to File3.txt")

os.rename("file2.txt", "file3.txt")
