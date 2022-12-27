from sys import stdin as s
from math import factorial


def main():
    number = int(s.readline().strip())
    while number != 0:
        frequencies = {str(i): 0 for i in range(10)}
        fact = str(factorial(number))
        for i in fact:
            frequencies[i] += 1
        print(format_ans(number, frequencies))
        number = int(s.readline().strip())


def format_ans(number, frequencies):
    response = f'{number}! --\n' + "   ({}){:>5} "*5
    response = response.strip() + "\n" + "   ({}){:>5} "*5
    values = []
    for i in frequencies:
        values.extend([i, frequencies[i]])
    return response.strip().format(*values)


main()

