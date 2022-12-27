from sys import stdin as s


def main():
    line = s.readline().strip()
    while line:
        speed, time = [int(i) for i in line.split()]
        print(speed*2*time)
        line = s.readline().strip()


main()
