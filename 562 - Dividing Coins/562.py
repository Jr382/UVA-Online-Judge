from sys import stdin as s


def main():
    cases = int(s.readline().strip())
    for i in range(cases):
        num_coins = int(s.readline().strip())
        coins = [int(i) for i in s.readline().split()]
        total = sum(coins)
        result = dp(num_coins, coins, total//2)
        print(total - 2*result)


def dp(num_values, values, capacity):
    memory = [0]*(capacity + 1)
    for i in range(1, num_values + 1):
        for value in range(capacity, 0, -1):
            if values[i-1] <= value:
                memory[value] = max(memory[value], memory[value - values[i - 1]] + values[i - 1])
            
    return memory[capacity]


main()
