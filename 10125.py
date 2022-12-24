from sys import stdin as s
from collections import defaultdict
from itertools import combinations


def main():
    set_len = int(s.readline().strip())
    while set_len != 0:
        subset = []
        for i in range(set_len):
            subset.append(int(s.readline().strip()))
        print(solve(subset))
        set_len = int(s.readline().strip())


def solve(subset):
    combs = list(combinations(subset, r=2))
    equations = defaultdict(default_value)
    for a, b in combs:
        result, diff = a+b, a-b
        equations[result][0].append((a, b))
        equations[diff][1].append((a, b))
        if diff < 0:
            equations[abs(diff)][1].append((b, a))
    solutions = []
    for eq in equations.values():
        if eq[0] and eq[1]:
            solutions.extend([i[0] for i in eq[1] if any([compare(i, j) for j in eq[0]])])

    return max(solutions) if solutions else "no solution"


def default_value():
    return [], []


def compare(tuple_1, tuple_2):
    return tuple_1[0] not in tuple_2 and tuple_1[1] not in tuple_2


main()
