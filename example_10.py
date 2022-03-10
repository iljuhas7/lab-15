import os
import time

with open("file3.txt", "w") as TextIO:
    TextIO.write("Null")

time.sleep(5)
os.remove("file3.txt")
