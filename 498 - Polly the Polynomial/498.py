from sys import stdin as s


def main():
    line = s.readline().strip()
    while line:
        coefficients = [int(i) for i in line.split()]
        x_values = [int(i) for i in s.readline().split()]
        results = []
        for x in x_values:
            result = coefficients[0]
            # Horner's method
            for i in coefficients[1:]:
                result = x*result + i
            results.append(result)
        print(*results)
        line = s.readline().strip()


main()
