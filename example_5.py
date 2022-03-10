TextIO = open("newfile.txt", "x")
print(TextIO)
if TextIO:
    print("File created successfully")
TextIO.close()
