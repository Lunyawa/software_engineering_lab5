#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print("Таблица умножения: ")

    for i in range(1, 10):
        for j in range(1, 10):
            res = f"{i} * {j} = {i * j}"
            print(res, end=(15 - len(res)) * " ")
        print()
