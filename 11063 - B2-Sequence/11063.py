from sys import stdin as s


def main():
    case = 1
    size = s.readline().strip()
    while size:
        array = [int(i) for i in s.readline().split()]
        is_b2 = b2_sequence(int(size), array)
        print("Case #{}: {}\n".format(case, is_b2))
        s.readline().strip()
        size = s.readline().strip()
        case += 1


def b2_sequence(size, array):
    sums = set()
    for i in range(size):
        if array[i] < 1:
            return "It is not a B2-Sequence."
        for j in range(i, size):
            current_size = len(sums)
            sums.add(array[i]+array[j])
            if array[i] > array[j] or len(sums) == current_size:
                return "It is not a B2-Sequence."
    else:
        return "It is a B2-Sequence."


main()
