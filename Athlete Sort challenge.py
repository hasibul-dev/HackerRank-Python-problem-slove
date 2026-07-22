#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])
    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    # Sort the list of rows based on the element at index k
    arr.sort(key=lambda row: row[k])

    # Print each sorted row separated by spaces
    for row in arr:
        print(*row)
