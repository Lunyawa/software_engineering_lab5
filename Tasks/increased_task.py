#!\usr\bin\env python3
# -*- coding: utf-8 -*-

import sys
import math

# Постоянная Эйлера.
EULER = 0.5772156649015328606
# Точность вычислений.
EPS = 1e-10

if __name__ == '__main__':
    x = float(input("Value of x? "))
    if x == 0:
        print("Illegal value of x", file=sys.stderr)
        exit(1)

    temp = x
    Sum = temp
    n = 1

    # Найти сумму членов ряда.
    while math.fabs(temp) > EPS:
        temp *= ((x**2) * (2 * n + 1)) / (((2 * n + 3)**2) * (2 * n + 2))
        Sum += temp
        n += 1

    # Вывести значение функции.
    print(f"Es({x}) = {EULER + math.log(math.fabs(x)) + Sum}")
