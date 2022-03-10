with open("file2.txt", "r") as TextIO:
    print("The TextIO is at byte :", TextIO.tell())
    TextIO.seek(10)
    print("After reading, the TextIO is at:", TextIO.tell())
