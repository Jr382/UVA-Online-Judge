from sys import stdin as s
from itertools import combinations


def main():
    size, case = int(s.readline().strip()), 1
    while size:
        ans, case, elements, queries = f'Case {case}:\n', case + 1, [], []
        for i in range(size):
            elements.append(int(s.readline().strip()))
        num_queries = int(s.readline().strip())
        for i in range(num_queries):
            queries.append(int(s.readline().strip()))
        ans += solve(elements, queries)
        print(ans.strip())
        size = int(s.readline().strip())


def solve(elements, queries):
    sums, used = sorted([comb[0] + comb[1] for comb in combinations(elements, 2)]), set()
    ans = ""
    for query in queries:
        closest_sum = bin_search(query, sums)
        if abs(query - sums[closest_sum]) > abs(query - sums[(closest_sum + 1) % len(sums)]):
            closest_sum += 1
        ans += f'Closest sum to {query} is {sums[closest_sum]}.\n'
    return ans.strip()


def bin_search(n, elements):
    left, right, i, aux = 0, len(elements), -1, -1
    while True:
        i = (left+right)//2
        if elements[i] == n:
            break
        elif elements[i] > n:
            right = i
        elif elements[i] < n:
            left = i
        if aux == i:
            break
        aux = i
    return i


main()
