from sys import stdin as s
swaps = 0


def main():
    global swaps
    # Simulating C++ input
    lines = s.readlines()
    raw_input = ""
    for line in lines:
        raw_input += line.replace("\n", " ")
    raw_input = raw_input.split()
    i = 0
    while i < len(raw_input):
        size, swaps, lis = int(raw_input[i]), 0, []
        i += 1
        for j in range(size):
            lis.append(int(raw_input[i]))
            i += 1
        merge_sort(lis)
        print(f'Minimum exchange operations : {swaps}')


def merge_sort(lis):
    global swaps
    size, merge = len(lis), lis
    if size > 1:
        left, right = merge_sort(lis[:size//2]), merge_sort(lis[size//2:])
        merge, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merge.append(left[i])
                i += 1
            else:
                swaps += len(left) - i
                merge.append(right[j])
                j += 1
        merge.extend(left[i:])
        merge.extend(right[j:])
    return merge


main()

