import io
import string
import sys
import os.path
import time

from encodings import utf_8

# Задание 2. Продолжая тему предыдущего упражнения, в тех же операционных системах на базе Unix обычно есть и утилита
# с названием tail, которая отображает последние десять строк содержимого файла, имя которого передается в качестве
# аргумента командной строки. Реализуйте программу, которая будет делать то же самое. В случае отсутствия файла,
# указанного пользователем, или аргумента командной строки вам нужно вывести соответствующее сообщение.


if len(sys.argv) <= 1:
    print("Error: No file arguments founds.")
    exit()

filenames = []
sleep = -1
lines = 2
size = 5
show_file = True
sl = False

t_key = 1
for key, curArg in enumerate(sys.argv):
    if key != t_key:
        if key < t_key:
            continue
        break
    t_key += 1

    if curArg[0:1] in "-":
        curArg = curArg[1:]
        if len(curArg) == 0:
            while True:
                pass

        if curArg not in ["c", "f", "n", "q", "d", "v"]:
            print("Error: unrecognized option -" + curArg)
            exit()

        if curArg in "c":
            if len(sys.argv) == (key + 1) or not sys.argv[key + 1].isdigit():
                print("Error: option requires an argument -- 'c'")
                exit()

            size = int(sys.argv[key + 1])
            sl = True
            t_key += 1

        if curArg in "n":
            if len(sys.argv) == (key + 1) or not sys.argv[key + 1].isdigit():
                print("Error: option requires an argument -- 'n'")
                exit()

            lines = int(sys.argv[key + 1])
            sl = False
            t_key += 1

        if curArg in "f":
            sleep = 1

        if curArg in "d":
            if len(sys.argv) == (key + 1) or not sys.argv[key + 1].isdigit():
                print("Error: option requires an argument -- 't'")
                exit()

            if sleep > -1:
                sleep = int(sys.argv[key + 1])

            t_key += 1

        if curArg in "q":
            show_file = False

        if curArg in "v":
            show_file = True

    else:
        if not os.path.isfile(curArg):
            print("Error: No file arguments founds.")
            exit()

        filenames.append(curArg)


file_last_time = []
while True:
    for key, filename in enumerate(filenames):
        if len(file_last_time) < key + 1:
            file_last_time.append(0)

        if os.path.getmtime(filename) != file_last_time[key]:
            file_last_time[key] = os.path.getmtime(filename)

            with open(filename, "r", encoding="windows-1251") as f:
                if show_file:
                    print("==> " + os.path.basename(filename) + " <==")

                if sl:
                    f.seek(0, io.SEEK_END)
                    f_size = f.tell()
                    f.seek(f_size - size, io.SEEK_SET)
                    print(f.read(size))

                else:
                    lns = list(f)
                    for line in lns[len(lns) - lines:]:
                        print(line, end="")

            print("\n")

    if sleep < 0:
        break

    time.sleep(sleep)