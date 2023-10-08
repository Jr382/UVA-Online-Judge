from sys import stdin as s


def main():
    cases = int(s.readline().strip())
    for i in range(cases):
        n, k = [int(i) for i in s.readline().split()]
        numbers = [int(i) % k for i in s.readline().split()]
        print(divisibility(k, numbers))


def divisibility(k, numbers):
    sums = generate_sums(k, numbers)
    return "Divisible" if bottom_up(numbers[0], k, sums) else "Not divisible"


def generate_sums(k, numbers):
    count, sums = {i: 0 for i in range(k)}, []
    for i in numbers[1:]:
        count[i] += 1
    for i in range(1, k):
        if count[i] > 0:
            sums.append([i * j for j in range(-1 * count[i], count[i] + 1, 2)])
    return sums


def bottom_up(n, k, sums):
    memory = {i: 0 for i in range(k)}
    memory[n] = True
    for i in sums:
        active = [i for i in memory if memory[i]]
        for result in active:
            memory[result] = False
            for j in i:
                memory[(result + j % k) % k] = True

    return memory[0]


main()

