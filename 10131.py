import sys
sys.setrecursionlimit(100000)
memory = {}


def main():
    elephants, counter = [], 1
    line = sys.stdin.readline().strip()
    while line:
        elephants.append([int(i) for i in line.split()]+[str(counter)])
        counter += 1
        line = sys.stdin.readline().strip()
    elephants.sort(key=lambda x: (x[0], -x[1]))
    largest = dp(elephants, (float("-inf"), float("inf")))
    print(str(len(largest))+"\n"+"\n".join(largest).strip())


def dp(remaining, last):
    global memory
    if last not in memory:
        taken, not_taken = [], []
        if len(remaining) > 0:
            not_taken = dp(remaining[1:], last)
            if compare(last, remaining[0]):
                taken = [remaining[0][2]] + dp(remaining[1:], tuple(remaining[0]))
        memory[last] = max(taken, not_taken, key=lambda x: len(x))

    return memory[last]


def compare(elephant1, elephant2):
    return elephant1[0] < elephant2[0] and elephant1[1] > elephant2[1]


main()
