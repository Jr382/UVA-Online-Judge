# from sys import stdin as s
from time import time

def main():
    line = s.readline().strip()
    while line != "0":
        n, q = [int(i) for i in line.split()]
        groups = group_by_number([int(i) for i in s.readline().split()])
        ans = []
        for _ in range(q):
            i, j = [int(i) - 1 for i in s.readline().split()]
            ans.append(solve(i, j, groups))
        print("\n".join(ans))
        line = s.readline().strip()


def group_by_number(numbers):
    groups = {}
    for i in range(len(numbers)):
        key = numbers[i]
        if key not in groups:
            groups[key] = [i, 0]
        groups[key][1] += 1

    return [(groups[i][0], groups[i][1]) for i in groups]


def solve(i, j, groups):
    lower_bound, upper_bound = bin_search(i, groups), bin_search(j, groups)
    relevant_groups = groups[lower_bound:upper_bound + 1]
    relevant_groups[0] = fix_group_bounds(relevant_groups[0], i, j)
    if len(relevant_groups) > 1:
        relevant_groups[-1] = fix_group_bounds(relevant_groups[-1], i, j)
    return str(max(relevant_groups, key=lambda x: x[1])[1])


def bin_search(n, elements):
    left, right, i, aux = 0, len(elements), -1, -1
    while True:
        i = (left + right) // 2
        if elements[i][0] == n:
            break
        elif elements[i][0] > n:
            right = i
        elif elements[i][0] < n:
            left = i
        if aux == i:
            break
        aux = i

    return i


def fix_group_bounds(group, lower_bound, upper_bound):
    total, group_upper_bound = group[1], group[0] + group[1] - 1
    total += (group[0] - lower_bound) if lower_bound > group[0] else 0
    total += (upper_bound - group_upper_bound) if group_upper_bound > upper_bound else 0

    return group[0], total


# main()
t1 = time()
s = open("test_case", "r")
line = s.readline()
while line != "0":
    n, q = [int(i) for i in line.split()]
    groups = group_by_number([int(i) for i in s.readline().split()])
    ans = []
    for _ in range(q):
        i, j = [int(i) - 1 for i in s.readline().split()]
        ans.append(solve(i, j, groups))
    #print("\n".join(ans))
    line = s.readline().strip()
print(time()-t1)