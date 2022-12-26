from sys import stdin as s
swaps = 0


def main():
    global swaps
    line = s.readline().strip()
    while line:
        lis, swaps = [int(i) for i in s.readline().split()], 0  # You have to simulate C++ input
        merge_sort(lis)
        print(f'Minimum exchange operations : {swaps}')
        line = s.readline().strip()


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

