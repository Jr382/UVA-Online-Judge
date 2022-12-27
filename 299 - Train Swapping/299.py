from sys import stdin as s


def main():
    cases = int(s.readline().strip())
    response = ""
    for case in range(cases):
        num_trains = int(s.readline().strip())
        trains = [int(i) for i in s.readline().split()]
        sorted_trains = sorted(trains)
        swaps = 0
        while trains != sorted_trains:
            for i in range(num_trains-1):
                if trains[i] > trains[i+1]:
                    trains[i], trains[i+1] = trains[i+1], trains[i]
                    swaps += 1
        response += f"Optimal train swapping takes {swaps} swaps.\n"
    print(response.strip())


main()
