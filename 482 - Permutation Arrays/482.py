from sys import stdin as s


def main():
    cases = int(s.readline().strip())
    for i in range(cases):
        s.readline()
        permutation = [int(i) - 1 for i in s.readline().split()]
        array = [i.strip() for i in s.readline().split(" ")]
        print(permute(permutation, array))
        if i+1<cases: print()


def permute(permutation, array):
    result = ["" for _ in range(len(array))]
    for i in range(len(array)):
        result[permutation[i]] = array[i]
    return "\n".join(result)


main()
