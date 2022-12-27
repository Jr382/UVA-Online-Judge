from sys import stdin as s

def main():
    line = s.readline().strip()
    response = ""
    while line != "0":
        n = int(line)
        result = n-10 if n > 101 else 91
        response += f'f91({line}) = {result}\n'
        line = s.readline().strip()
    print(response.strip())

main()
