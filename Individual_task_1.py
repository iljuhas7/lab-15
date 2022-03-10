
# Задание 1. Написать программу, которая считывает текст из файла и выводит на экран только предложения, содержащие
# введенное с клавиатуры слово.

word = input("Введите слово: ")

with open("text2.txt", "r", encoding="utf-8") as f:
    for line in f:
        words = line.split(" ")
        for zword in words:
            if word in zword:
                print(line)
