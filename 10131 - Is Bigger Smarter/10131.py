import sys
sys.setrecursionlimit(100000)


def main():
    elephants, counter = [], 1
    line = sys.stdin.readline().strip()
    while line:
        elephants.append([int(i) for i in line.split()]+[str(counter)])
        counter += 1
        line = sys.stdin.readline().strip()
    elephants.sort(key=lambda x: (x[0], -x[1]))
    response = dp(elephants)
    print("{}\n{}".format(len(response), "\n".join(response).strip()))


def memoization(function):
    memory = {}

    def wrapper(remaining, last=(float("-inf"), float("inf"))):
        if last not in memory:
            memory[last] = function(remaining, last)
        return memory[last]

    return wrapper


@memoization
def dp(remaining, last):
    ans = []
    if len(remaining) > 0:
        not_taken = dp(remaining[1:], last)
        taken = [remaining[0][2]] + dp(remaining[1:], tuple(remaining[0])) if compare(last, remaining[0]) else []
        ans = max(taken, not_taken, key=lambda x: len(x))
    return ans


def compare(elephant1, elephant2):
    return elephant1[0] < elephant2[0] and elephant1[1] > elephant2[1]


main()
