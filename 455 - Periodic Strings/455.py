from sys import stdin as s


def main():
    cases = int(s.readline().strip())
    response = ""
    for i in range(cases):
        s.readline().strip()
        line = s.readline().strip()
        response += f'{smaller_period(line)}\n\n'
    print(response.strip())


def smaller_period(string):
    substring = ""
    for i in string:
        substring += i
        if len(string) % len(substring) == 0 and substring*(len(string)//len(substring)) == string:
            break
    return len(substring)


main()
