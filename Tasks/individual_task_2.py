#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a, b, c = map(int, input("Enter 3 numbers: ").split())

    if (a % 2 == 0) or (b % 2 == 0) or (c % 2 == 0):
        print("Yes, there are even numbers among the three given numbers")
    else:
        print("There are no even numbers among the three given numbers")
