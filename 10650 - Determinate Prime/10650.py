from sys import stdin as s
prime_sets = []


def main():
    global prime_sets
    prime_sets = determinate_primes()
    line = sorted([int(i) for i in s.readline().split()])
    while line != [0, 0]:
        lower, upper = bin_search(line[0]), bin_search(line[1])
        sets = [" ".join(map(lambda x: str(x), prime_sets[i]))
                for i in range(lower, upper+1)
                if prime_sets[i][0] >= line[0] and prime_sets[i][-1] <= line[1]]
        if len(sets) > 0:
            print("\n".join(sets))
        line = sorted([int(i) for i in s.readline().split()])


def determinate_primes():
    primes = get_primes(32000)
    sets, subset, distance = [], [primes[0], primes[1]], primes[1] - primes[0]
    for i in range(1, len(primes)-1):
        if primes[i+1] - primes[i] == distance:
            subset.append(primes[i+1])
        else:
            if len(subset) >= 3:
                sets.append(subset)
            subset = [primes[i], primes[i+1]]
            distance = primes[i+1] - primes[i]

    return sets


def get_primes(n):
    primes = []
    sieve = [True] * n
    for number in range(2, n):
        if sieve[number]:
            primes.append(number)
            for no_prime in range(number * number, n, number):
                sieve[no_prime] = False
    return primes


def bin_search(n):
    global prime_sets
    left, right, i, aux = 0, len(prime_sets), -1, -1
    while True:
        i = (left + right) // 2
        if prime_sets[i][0] == n:
            break
        elif prime_sets[i][0] < n:
            left = i
        elif prime_sets[i][0] > n:
            right = i
        if aux == i:
            break
        aux = i
    return i


main()
