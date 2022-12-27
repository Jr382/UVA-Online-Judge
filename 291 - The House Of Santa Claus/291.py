ways = []
graph = [(1, 2, 4), (0, 2, 4), (0, 1, 3, 4), (2, 4), (0, 1, 2, 3)]


def main():
    global ways
    bfs()
    response = "\n".join(ways).strip()
    print(response)


def bfs(start=0, used=[], path="1"):
    global ways, graph
    if len(path) == 9:
        ways.append(path)
    else:
        for node in graph[start]:
            if f'{start}{node}' not in used:
                bfs(node, used + [f'{start}{node}', f'{node}{start}'], path + str(node + 1))


main()
