#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    n = int(input("Value of n: "))
    if n <= 0:
        print("Illegal value of n", file=sys.stderr)
        exit(1)

    if n <= 250:
        print("Price = 7 rubles per hour")
    elif n <= 300:
        print("Price = 17 rubles per hour")
    else:
        print("Price = 20 rubles per hour")
