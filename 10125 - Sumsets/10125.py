from sys import stdin as s
from itertools import combinations
subset = []


def main():
    global subset
    set_len = int(s.readline().strip())
    while set_len != 0:
        subset = []
        for i in range(set_len):
            subset.append(int(s.readline().strip()))
        print(solve())
        set_len = int(s.readline().strip())


def solve():
    global subset
    combs, differences, results = list(combinations(subset, r=2)), [], {}
    for a, b in combs:
        result, diff = a + b, a - b
        if result not in results:
            results[result] = []
        results[result].append((a, b))
        differences.append((diff, a, b))
        if diff < 0:
            differences.append((abs(diff), b, a))
    differences.sort(key=lambda x: x[1], reverse=True)
    for diff, d, c in differences:
        if diff in results:
            for a, b in results[diff]:
                if len({a, b, c, d}) == 4:
                    return d

    return "no solution"


main()

