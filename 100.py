from sys import stdin as s

def main():
    global memory
    memory = {1:1}
    line = s.readline().strip()
    response = ""
    while line:
        i, j = sorted([int(i) for i in line.split(" ")])
        max_cycle = max([function(i) for i in range(i, j+1)])
        response += "{} {}\n".format(line, max_cycle)
        line = s.readline().strip()
    print(response.strip())

def function(n):
    global memory
    if n not in memory:
        memory[n] = 1 + function(3*n+1 if n%2 != 0 else n//2)
    return memory[n]

main()


        
