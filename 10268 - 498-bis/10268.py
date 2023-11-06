from sys import stdin as s


def main():
    line = s.readline().strip()
    while line:
        x = int(line)
        coefficients = s.readline().split()
        coefficients = [int(coefficients[i])*(len(coefficients)-1-i) for i in range(len(coefficients))]
        result = coefficients[0]
        # Horner's method
        for i in coefficients[1:-1]:
            result = x*result + i
        print(result)
        line = s.readline().strip()


main()
