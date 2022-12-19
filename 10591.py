from sys import stdin as s


def main():
    cases = int(s.readline().strip())
    for i in range(cases):
        number = int(s.readline().strip())
        print("Case #{}: {} is {} number.".format(i+1, number, happy_number(number)))


def happy_number(n):
    visited = set()
    while n != 1:
        n = sum([int(i)**2 for i in str(n)])
        if n in visited:
            break
        visited.add(n)
    return "a Happy" if n == 1 else "an Unhappy"


main()
