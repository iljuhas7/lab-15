#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with open("text.txt", "r", encoding="utf-8") as f:
        sentences = f.readlines()

    for sentence in sentences:
        if "," in sentence:
            print(sentence)
