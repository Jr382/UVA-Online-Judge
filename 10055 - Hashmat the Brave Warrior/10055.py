from sys import stdin as s


def main():
    line = s.readline().strip()
    while line:
        armies = [int(i) for i in line.split()]
        print(abs(armies[0]-armies[1]))
        line = s.readline().strip()


main()
