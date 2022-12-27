from sys import stdin as s


def main():
    cases = int(s.readline().strip())
    for i in range(cases):
        farmers = int(s.readline().strip())
        total_premium = 0
        for j in range(farmers):
            data = [int(i) for i in s.readline().split()]
            total_premium += data[0]*data[2]
        print(total_premium)


main()
