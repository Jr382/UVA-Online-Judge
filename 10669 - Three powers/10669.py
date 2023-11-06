from sys import stdin as s
from math import log2


def main():
    line = int(s.readline().strip())
    while line != 0:
        if line == 1:
            print("{ }")
        else:
            print(solve(line-1))
        line = int(s.readline().strip())


def solve(n):
    subset = []
    while n > 0:
        power = int(log2(n))
        subset.append(str(3 ** power))
        n -= int(2**power)
    return "{{ {} }}".format(", ".join(reversed(subset)))


main()
