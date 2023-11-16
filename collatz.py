#!/usr/bin/env python

def collcount(n):
    """Count how many steps it takes to get to 1"""
    count = 0
    while n != 1:
        if n & 1:
            n = 3 * n + 1
        else:
            n = n // 2
        count += 1
    return count

if __name__ == '__main__':
    max_ = -1
    for n in range(1, 10000000):
        c = collcount(n)
        if c > max_:
            max_ = c
            print(n, c)


