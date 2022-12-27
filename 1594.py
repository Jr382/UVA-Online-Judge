from sys import stdin as s


def main():
    cases = int(s.readline().strip())
    for i in range(cases):
        size = int(s.readline().strip())
        start = tuple(int(i) for i in s.readline().split())
        print("ZERO" if size in [2, 4, 8] else solve(start))


def solve(step):
    # No fucking idea
    size, visited = len(step), set()
    while any(step) and step not in visited:
        visited.add(step)
        step = tuple(abs(step[i] - step[(i + 1) % size]) for i in range(size))
    return "ZERO" if not any(step) else "LOOP"


main()
