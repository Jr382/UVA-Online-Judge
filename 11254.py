from sys import stdin as s


def main():
    number = int(s.readline().strip())
    while number != -1:
        print("{} = {} + ... + {}".format(number, *solve(number)))
        number = int(s.readline().strip())


def solve(n):
    for i in range(int((n*2)**0.5), 0, -1):
        t1, t2 = (2*n - i*(i-1)), 2*i
        if t1 % t2 == 0:
            a = t1 // t2
            return a, a + i - 1


main()
