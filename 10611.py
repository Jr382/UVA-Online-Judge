from sys import stdin as s

def main():
    global ladies
    num_ladies = int(s.readline().strip())
    ladies = list(set([int(i) for i in s.readline().strip().split()]))
    ladies.sort()
    num_queries = s.readline()
    queries = [int(i) for i in s.readline().strip().split()]
    response = ""
    for q in queries:
        i, j = bin_search(q)
        response += "{} {}\n".format(
                ladies[i] if i >= 0 else "X",
                ladies[j] if j < len(ladies) else "X")
    print(response.strip())
            
def bin_search(n):
    global ladies
    l, r, i, aux = 0, len(ladies), -1, -1
    while True:
        i = (l+r)//2
        if ladies[i] == n:
            break
        elif ladies[i] > n:
            r = i
        elif ladies[i] < n:
            l = i
        if aux == i:
            break
        aux = i
    chosen_ladies = (i-1, i+1)
    if ladies[i] < n: chosen_ladies = (i, i+1)
    elif ladies[i] > n: chosen_ladies = (i-1, i)
    return chosen_ladies

main()
